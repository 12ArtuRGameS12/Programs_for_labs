import unittest
from lib_lab import *


class Testtest_lib_lab(unittest.TestCase):
	def test_clr_sp(self):
		self.assertEqual(clr_sp("  12,3 21   4 "), "12,3 21 4")
		self.assertEqual(clr_sp("    123,25  125 6,47 "), "123,25 125 6,47")
		self.assertEqual(clr_sp("124, 1246  ,  46 "), "124,1246,46")
		self.assertEqual(clr_sp("1.24, 12.46  ,  46 "), "1.24,12.46,46")
		with self.assertRaises(TypeError):
			clr_sp(1234)
