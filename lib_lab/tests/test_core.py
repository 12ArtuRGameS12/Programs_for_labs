from unittest import TestCase
from lib_lab.core import *


class Test_core(TestCase):

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
        self.assertEqual(mnc([1, 2, 3], [0.4, 0.5, 0.6]), (0.9999999999999999,
                                                           (0.09999999999999994, 9.974797390018023e-16),
                                                           (0.3000000000000001, 2.2515752320326228e-07)))
        self.assertEqual(mnc([1, 2, 3], [1, 2, 3], 2, 2), (0.9999999999999998, (1.0, 0.0)))

        self.assertRaisesRegex(TypeError, "arg1 - str не tuple или list", mnc, "1234", [1, 2, 3])
        self.assertRaisesRegex(ValueError, "Нету такой формулы 5", mnc, [1, 2, 3], [1, 2, 3], 2, 5)
        self.assertRaisesRegex(ValueError, "Меньше трёх нельзя в режиме 1", mnc, [1, 2], [1, 2])

    def test_cosn_izmer_formula(self):
        self.assertEqual(cosn_izmer_formula("a**3 + b*2", "a", "b"), "sqrt(9*a**4*da**2 + 4*db**2)")
        self.assertEqual(cosn_izmer_formula("123", "a", "b"), "0")

        self.assertRaisesRegex(TypeError, "123 - int не str", cosn_izmer_formula, 123, "1")
        self.assertRaisesRegex(TypeError, "2 - int не str", cosn_izmer_formula, "a*5", "b", 1234)

    def test_convert2number(self):
        self.assertEqual(convert2number("12.3"), 12.3)

        self.assertRaisesRegex(TypeError, "num_str - int не str", convert2number, 1234)

    def test_formul_exe(self):
        self.assertEqual(formul_exe("sqrt(9*a**4*da**2 + 4*db**2)", {"a": 4, "da": 2, "b": 5, "db": 1}),
                         (96.0208310732624, "2*sqrt(2305)"))

        self.assertRaisesRegex(TypeError, "formul - int не str", formul_exe, 1234, {"a": 5})
        self.assertRaisesRegex(TypeError, "varabels - int не dict", formul_exe, "a+b", 1234)
        self.assertRaisesRegex(TypeError, "1 - int не str", formul_exe, "a+b", {1234: 5})
