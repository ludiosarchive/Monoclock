#!/usr/bin/env python

import os
import sys
import unittest


def getSuite():
	suite = unittest.TestLoader().loadTestsFromNames([
		'test_monoclock.MonoclockTests',
	])
	return suite


def main():
	runner = unittest.TextTestRunner()
	suite = getSuite()
	runner.run(suite)


def _parent(path):
	return os.path.dirname(path)


if __name__ == '__main__':
	packageParentDir = _parent(os.path.abspath(__file__))
	sys.path.insert(0, packageParentDir)
	print "sys.path[0] is now", repr(sys.path[0])
	print
	print "Note that unittest swallows import-time exceptions.  If you see an"
	print "exception below, it might be masking some other exception."
	print "=" * 78
	main()
