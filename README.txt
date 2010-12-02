Overview
========

Monoclock is a Python module that provides access to the
monotonic clock on POSIX-like OSes that have `librt`.

Compatibility: tested on CPython 2.6.5, CPython 2.7, pypy 1.3,
and pypy 1.4.

To install:
$ python setup.py install

To run the tests:
$ python run_tests.py


Usage
=====
import monoclock
t = monoclock.nano_count()

If you want seconds, divide t by 1e9.


Misc
====
Assorted collection of monotonic clock references:
- http://code-factor.blogspot.com/2009/11/monotonic-timers.html
- Factor's source code.
- Chromium's source code.
