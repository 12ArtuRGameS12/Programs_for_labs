from unittest import TestCase
from lib_lab import *


class Testtest_lib_lab(TestCase):
	def test_clr_sp(self):
		self.assertEqual(clr_sp("  12,3 21   4 "), "12,3 21 4")
		self.assertEqual(clr_sp("    123,25  125 6,47 "), "123,25 125 6,47")
		self.assertEqual(clr_sp("124, 1246  ,  46 "), "124,1246,46")
		self.assertEqual(clr_sp("1.24, 12.46  ,  46 "), "1.24,12.46,46")

		self.assertRaisesRegex(TypeError, "text - int не str", clr_sp, 1234)

	def test_stu(self):
		self.assertEqual(stu(4), 2.776)
		self.assertEqual(stu(4, 2), 2.776)
		self.assertEqual(stu(4, 3), 4.604)

		self.assertRaisesRegex(ValueError, "Нету в таблице такой доверительной вероятности как 4", stu, 9999, 4)
		self.assertRaisesRegex(ValueError, "Нету в таблице такой степени свободы как 9998", stu, 9998, 3)
		self.assertRaisesRegex(TypeError, "n - str не int", stu, "1234")

	def test_rotate(self):
		self.assertEqual(rotate([[1, 2, 3, 4], [5, 6, 7, 8]]), [[1, 5], [2, 6], [3, 7], [4, 8]])
		self.assertEqual(rotate(((1, 2, 3, 4), (5, 6, 7, 8))), ((1, 5), (2, 6), (3, 7), (4, 8)))
		self.assertRaisesRegex(TypeError, "tabel - int не tuple или list", rotate, 1234)

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

		self.assertRaisesRegex(TypeError, "arg1 - int не tuple или list", stat, 1234)
		self.assertRaisesRegex(TypeError, "arg2 - int не tuple или list", stat, (1, 2, 3), 1234)
		self.assertRaisesRegex(TypeError, "2 - str не int или float", stat, (1, 2, "3"), 1234)
		self.assertRaisesRegex(ValueError, "Меньше двух нельзя", stat, tuple())
		self.assertRaisesRegex(ValueError, "Меньше двух нельзя", stat, (1,))

	def test_prim_izmer(self):
		self.assertEqual(prim_izmer((1, 2, 3), 0.5, 1), (2.0, 1.7080107418996064))
		self.assertEqual(prim_izmer((1, 2, 3), 0.5), (2.0, 2.5057229384839106))
		self.assertEqual(prim_izmer((1, 2, 3), 0.5, 1, True), {
			'obp': 1.7080107418996064, 'prp': 0.27416666666666667, 'slp': 1.685862786033707})

		self.assertRaisesRegex(TypeError, "data - int не tuple или list", prim_izmer, 1234, 0.5)
		self.assertRaisesRegex(TypeError, "2 - str не int или float", prim_izmer, (1, 2, "3"), 0.5)
		self.assertRaisesRegex(TypeError, "accuracy - str не int или float", prim_izmer, (1, 2, 3), "1234")
		self.assertRaisesRegex(TypeError, "debug - int не bool", prim_izmer, (1, 2, 3), 0.5, 1, 1234)

	def test_nerav_izmer(self):
		self.assertEqual(nerav_izmer(
			[1, 2, 3], [0.4, 0.5, 0.6]), (1.7334754797441363, 0.479872051177255))

		self.assertRaisesRegex(TypeError, "data - str не tuple или list", nerav_izmer, "1234", [0.4, 0.5, 0.6])
		self.assertRaisesRegex(TypeError, "2 - str не int или float", nerav_izmer, [1, 2, "3"], [0.4, 0.5, 0.6])
		self.assertRaisesRegex(TypeError, "debug - str не bool", nerav_izmer, [1, 2, 3], [0.4, 0.5, 0.6], "1234")

	def test_mnc(self):
		self.assertEqual(mnc([1, 2, 3], [0.4, 0.5, 0.6]), (
			0.9999999999999999, (0.09999999999999994, 9.974797390018023e-16), (0.3000000000000001, 2.2515752320326228e-07)))
		self.assertEqual(mnc([1, 2, 3], [1, 2, 3], 2), (0.9999999999999998, (1.0, 0.0)))

		self.assertRaisesRegex(TypeError, "arg1 - str не tuple или list", mnc, "1234", [1, 2, 3])
		self.assertRaisesRegex(TypeError, "debug - str не bool", mnc, [1, 2, 3], [0.4, 0.5, 0.6], 1, "1234")
		self.assertRaisesRegex(ValueError, "Нету такой формулы 5", mnc, [1, 2, 3], [1, 2, 3], 5)
		self.assertRaisesRegex(ValueError, "Меньше трёх нельзя в режиме 1", mnc, [1, 2], [1, 2])

	def test_cosn_izmer_formul(self):
		self.assertEqual(cosn_izmer_formul("a**3 + b*2", "a", "b"), "sqrt(9*a**4*da**2 + 4*db**2)")
		self.assertEqual(cosn_izmer_formul("123", "a", "b"), "0")

		self.assertRaisesRegex(TypeError, "123 - int не str", cosn_izmer_formul, 123, "1")
		self.assertRaisesRegex(TypeError, "2 - int не str", cosn_izmer_formul, "a*5", "b", 1234)

	def test_convert2number(self):
		self.assertEqual(convert2number("12.3"), 12.3)

		self.assertRaisesRegex(TypeError, "num_str - int не str", convert2number, 1234)

	def test_formul_exe(self):
		self.assertEqual(formul_exe(
			"sqrt(9*a**4*da**2 + 4*db**2)", {"a": 4, "da": 2, "b": 5, "db": 1}), (96.0208310732624, "2*sqrt(2305)"))

		self.assertRaisesRegex(TypeError, "formul - int не str", formul_exe, 1234, {"a": 5})
		self.assertRaisesRegex(TypeError, "varabels - int не dict", formul_exe, "a+b", 1234)
		self.assertRaisesRegex(TypeError, "1 - int не str", formul_exe, "a+b", {1234: 5})
