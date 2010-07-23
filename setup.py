#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

setup(
	name='Monoclock',
	version='10.1.4',
	description="Monotonic clock access for Python",
	ext_modules = [
		Extension("monoclock", ["monoclock.c"], libraries=['rt']),
	],
)
