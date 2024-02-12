from unittest import TestCase
from lib_lab.tools import *


class Test_tools(TestCase):
    def test_clr_sp(self):
        self.assertEqual(clr_sp("  12,3 21   4 "), "12,3 21 4")
        self.assertEqual(clr_sp("    123,25  125 6,47 "), "123,25 125 6,47")
        self.assertEqual(clr_sp("124, 1246  ,  46 ", ","), "124,1246,46")
        self.assertEqual(clr_sp("1.24, 12.46 = ,  46 ", ",", "="), "1.24,12.46=,46")

        self.assertRaisesRegex(TypeError, "text - int не str", clr_sp, 1234)
        self.assertRaisesRegex(TypeError, "1 - int не str", clr_sp, "1.24, 12.46 = ,  46 ", 123)

    def test_sup_rep(self):
        self.assertEqual(sup_rep("123,l.dd,ww,1", {",": ".", ".": ","}), "123.l,dd.ww.1")

        self.assertRaisesRegex(TypeError, "text - int не str", sup_rep, 1234, {",": ".", ".": ","})
        self.assertRaisesRegex(TypeError, "1 - int не str", sup_rep, "1234", {1234: ".", ".": ","})
        self.assertRaisesRegex(TypeError, "0 - int не str", sup_rep, "1234", {",": 1234, ".": ","})

    def test_rotate(self):
        self.assertEqual(rotate([[1, 2, 3, 4], [5, 6, 7, 8]]), [[1, 5], [2, 6], [3, 7], [4, 8]])
        self.assertEqual(rotate(((1, 2, 3, 4), (5, 6, 7, 8))), ((1, 5), (2, 6), (3, 7), (4, 8)))
        self.assertRaisesRegex(TypeError, "tabel - int не tuple или list", rotate, 1234)

    def test_convert2number(self):
        self.assertEqual(convert2number("12.3"), 12.3)

        self.assertRaisesRegex(TypeError, "num_str - int не str", convert2number, 1234)
