Overview
========

Monoclock is a Python module that provides access to the
monotonic clock on POSIX-like OSes that have `librt`.

Compatibility: tested on CPython 2.6.5, CPython 2.7, pypy 1.3,
and pypy 1.4.

Install: `python setup.py install`

Run the tests: `python run_tests.py`


Usage
=====

```
import monoclock
t = monoclock.nano_count()
print t
```

If you want seconds, divide `t` by `1e9`.


Misc
====

If you're having trouble with monotonic clocks, see:

*	http://code-factor.blogspot.com/2009/11/monotonic-timers.html

*	Factor's source code.

*	Chromium's source code.


Wishlist
========
*	OS X support (no librt, but mostly the same, I think)

*	Windows support.

*	Solaris support (does it work?).

*	Expose `CLOCK_MONOTONIC_RAW` (which is not adjusted by NTP).

*	Support buggy AMD chips, or expose a `probablyBuggy()`
	function that returns `True` if the monotonic clock is
	unreliable.

	Note: Chromium's `base/time_win.cc` just disables use of the
	monotonic clock on Athlon X2 CPUs with
	`if (cpu.vendor_name() == "AuthenticAMD" && cpu.family() == 15`
