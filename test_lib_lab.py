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

	def test_stu(self):
		self.assertEqual(stu(4), 2.776)
		self.assertEqual(stu(4, 2), 2.776)
		self.assertEqual(stu(4, 3), 4.604)
		with self.assertRaises(ValueError) as err:
			stu(9999, 4)
		self.assertEqual(err.exception.args[0], "Нету в таблице такой доверительной вероятности как 4")
		with self.assertRaises(ValueError) as err:
			stu(9998, 3)
		self.assertEqual(err.exception.args[0], "Нету в таблице такой степени свободы как 9998")

	def test_rotate(self):
		self.assertEqual(rotate([[1, 2, 3, 4], [5, 6, 7, 8]]), [[1, 5], [2, 6], [3, 7], [4, 8]])
		self.assertEqual(rotate(((1, 2, 3, 4), (5, 6, 7, 8))), ((1, 5), (2, 6), (3, 7), (4, 8)))
		with self.assertRaises(TypeError) as err:
			rotate(1234)
		self.assertEqual(err.exception.args[0], "<class 'int'> не tuple или list")
