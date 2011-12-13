#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

setup(
	name='Monoclock',
	version='11.5.3',
	description="Monotonic clock access for Python",
	url="https://github.com/ludios/Monoclock",
	author="Ivan Kozik",
	author_email="ivan@ludios.org",
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Operating System :: POSIX :: Linux',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
	],
	ext_modules=[
		Extension("monoclock", ["monoclock.c"], libraries=['rt']),
	],
)
