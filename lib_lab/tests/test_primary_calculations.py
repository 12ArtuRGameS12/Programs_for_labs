from unittest import TestCase
from lib_lab.primary_calculations import *


class Test_primary_calculations(TestCase):
    def test_stu(self):
        self.assertEqual(stu(4), 2.776)
        self.assertEqual(stu(4, 2), 2.776)
        self.assertEqual(stu(4, 3), 4.604)

        self.assertRaisesRegex(ValueError, "Нету в таблице такой доверительной вероятности как 4", stu, 9999, 4)
        self.assertRaisesRegex(ValueError, "Нету в таблице такой степени свободы как 9998", stu, 9998, 3)
        self.assertRaisesRegex(TypeError, "n - str не int", stu, "1234")

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
