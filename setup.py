#!/usr/bin/env python

import sys
from distutils.core import setup
from distutils.extension import Extension

if sys.platform == 'darwin':
	monoclock_libraries = []
else:
	monoclock_libraries = ['rt']

setup(
	name='Monoclock',
	version='14.4.16',
	description="Monotonic clock access for Python",
	url="https://github.com/ludios/Monoclock",
	author="Ivan Kozik",
	author_email="ivan@ludios.org",
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Operating System :: POSIX :: Linux',
		'Operating System :: MacOS :: MacOS X'
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
	],
	ext_modules=[
		Extension("monoclock", ["monoclock.c"], libraries=monoclock_libraries),
	],
)
