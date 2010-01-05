import unittest

import monoclock
import time

class MonoclockTests(unittest.TestCase):

	def test_nano_count_isCorrectType(self):
		val1 = monoclock.nano_count()
		self.assert_(isinstance(val1, (int, long)))


	def test_nano_count_getsBigger(self):
		values = []
		for n in xrange(10000):
			values.append(monoclock.nano_count())

		copied = sorted(values)
		self.assertEqual(values, copied)


	def test_wrongArguments(self):
		self.assertRaises(TypeError, lambda: monoclock.nano_count(1))
		self.assertRaises(TypeError, lambda: monoclock.nano_count(None))
		self.assertRaises(TypeError, lambda: monoclock.nano_count([]))
		self.assertRaises(TypeError, lambda: monoclock.nano_count({}))
		self.assertRaises(TypeError, lambda: monoclock.nano_count(keyword=1))
