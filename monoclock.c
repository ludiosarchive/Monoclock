#include <Python.h>
#include <time.h>

#ifdef __MACH__
#include <mach/mach.h>
#include <mach/mach_time.h>
#endif

static PyObject *
nano_count(PyObject *self, PyObject *args) {
	struct timespec t;
	int ret;
	PY_LONG_LONG nanoseconds;

	if(!PyArg_ParseTuple(args, "")) {
		return NULL;
	}

#ifdef __MACH__
	static mach_timebase_info_data_t timebase_info;
	if (timebase_info.denom == 0) {
		mach_timebase_info(&timebase_info);
	}
	uint64_t ticks = mach_absolute_time();
	/* Divide first then multiply to avoid overflows */
	ticks /= timebase_info.denom;
	ticks *= timebase_info.numer;
	t.tv_sec = ticks / (1000 * 1000 * 1000);
	t.tv_nsec = ticks % (1000 * 1000 * 1000);
	ret = 0;
#else
	ret = clock_gettime(CLOCK_MONOTONIC, &t);
#endif

	if(ret != 0) {
		PyErr_SetString(PyExc_SystemError,
			"clock_gettime failed");
		return NULL;
	}
	nanoseconds = (PY_LONG_LONG)t.tv_sec * 1000000000 + t.tv_nsec;
	return PyLong_FromUnsignedLongLong(nanoseconds);
}


static PyMethodDef MonoclockMethods[] = {
	{"nano_count", nano_count, METH_VARARGS,
	"Get the monotonic clock value, in nanoseconds."},
	{NULL, NULL, 0, NULL} /* Sentinel */
};


PyMODINIT_FUNC
initmonoclock(void)
{
	(void) Py_InitModule("monoclock", MonoclockMethods);
}
