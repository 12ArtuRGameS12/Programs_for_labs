from unittest import TestCase
from lib_lab import *


class Testtest_lib_lab(TestCase):
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

	def test_stat(self):
		self.assertEqual(stat([1, 2, 3], [3, 4, 5]), {
			'nX': 3,
			'srX': 2.0,
			's0X': 0.5773502691896257,
			'sumX': 6,
			'X2': [1, 4, 9],
			'sumX2': 14,
			'XX': [-1.0, 0.0, 1.0],
			'sumXX': 0.0,
			'XX2': [1.0, 0.0, 1.0],
			'sumXX2': 2.0,

			'nY': 3,
			'srY': 4.0,
			's0Y': 0.5773502691896257,
			'sumY': 12,
			'Y2': [9, 16, 25],
			'sumY2': 50,
			'YY': [-1.0, 0.0, 1.0],
			'sumYY': 0.0,
			'YY2': [1.0, 0.0, 1.0],
			'sumYY2': 2.0,

			'XY': [3, 8, 15],
			'sumXY': 26,
			'XXYY': [1.0, 0.0, 1.0],
			'sumXXYY': 2.0,
		})
		self.assertEqual(stat([1, 2, 3]), {
			'nX': 3,
			'srX': 2.0,
			's0X': 0.5773502691896257,
			'sumX': 6,
			'X2': [1, 4, 9],
			'sumX2': 14,
			'XX': [-1.0, 0.0, 1.0],
			'sumXX': 0.0,
			'XX2': [1.0, 0.0, 1.0],
			'sumXX2': 2.0,
		})

		with self.assertRaises(TypeError) as err:
			stat(1234)
		self.assertEqual(err.exception.args[0], "arg1 <class 'int'> не tuple или list")

		with self.assertRaises(TypeError) as err:
			stat((1, 2, 3), 1234)
		self.assertEqual(err.exception.args[0], "arg2 <class 'int'> не tuple или list")

		with self.assertRaises(ValueError) as err:
			stat(tuple())
		self.assertEqual(err.exception.args[0], "Меньше двух нельзя")

		with self.assertRaises(ValueError) as err:
			stat((1,))
		self.assertEqual(err.exception.args[0], "Меньше двух нельзя")

	def test_prim_izmer(self):
		self.assertEqual(prim_izmer((1, 2, 3), 0.5, 1), (2.0, 1.7080107418996064))
		self.assertEqual(prim_izmer((1, 2, 3), 0.5), (2.0, 2.5057229384839106))
		self.assertEqual(prim_izmer((1, 2, 3), 0.5, 1, True), {
			'obp': 1.7080107418996064, 'prp': 0.27416666666666667, 'slp': 1.685862786033707})

		with self.assertRaises(TypeError) as err:
			prim_izmer((1, 2, 3), 0.5, 1, 1234)
		self.assertEqual(err.exception.args[0], "debug <class 'int'> не bool")

		with self.assertRaises(TypeError) as err:
			prim_izmer(1234, 0.5)
		self.assertEqual(err.exception.args[0], "data <class 'int'> не tuple или list")

		with self.assertRaises(TypeError) as err:
			prim_izmer((1, 2, 3), "1234")
		self.assertEqual(err.exception.args[0], "accuracy <class 'str'> не int или float")

	# def test_(self):
	# 	self.assertEqual()
	#
	# 	with self.assertRaises() as err:
	#
	# 	self.assertEqual(err.exception.args[0], "")
