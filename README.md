Monoclock
=========

Monoclock is a fast Python module that provides access to the
monotonic clock on Linux and OS X.

Compatibility: tested on CPython 2.6.5, CPython 2.7, pypy 1.3,
and pypy 1.4.



Usage
=====

```
import monoclock
t = monoclock.nano_count()
print t
```

If you want seconds, divide `t` by `1e9`.



Installation
============

Make sure you have a C compiler and Python headers installed.  On Ubuntu,
that can be done with

```
sudo apt-get install python-dev build-essential
```

Then, install Monoclock from PyPi:

```
pip install --user Monoclock
```

or from the git repo:

```
git clone https://github.com/ludios/Monoclock
cd Monoclock
pip install --user .
```

or without pip:

```
python setup.py install --user
```

You should now have the `monoclock` module installed.

Optionally, run the tests with `python run_tests.py`



Misc
====

If you're having trouble with monotonic clocks, see:

*	http://code-factor.blogspot.com/2009/11/monotonic-timers.html

*	Factor's source code.

*	Chromium's source code.



Wishlist
========

*	Windows support.

*	Solaris support (does it work?).

*	Expose `CLOCK_MONOTONIC_RAW` (which is not adjusted by NTP).

*	Support buggy AMD chips, or expose a `probablyBuggy()`
	function that returns `True` if the monotonic clock is
	unreliable.

	Note: Chromium's `base/time_win.cc` just disables use of the
	monotonic clock on Athlon X2 CPUs with
	`if (cpu.vendor_name() == "AuthenticAMD" && cpu.family() == 15`



Contributing
============

Patches and pull requests are welcome.

This coding standard applies: http://ludios.org/coding-standard/
