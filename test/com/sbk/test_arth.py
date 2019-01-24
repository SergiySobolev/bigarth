import unittest

from parameterized import parameterized

from com.sbk.arth import quo_rem, add, mul


class TestArth(unittest.TestCase):

    @parameterized.expand([
        ['1', 7, 5, 1, 2],
        ['2', 16, 7, 2, 2],
        ['3', 2, 7, 0, 2]

    ])
    def test_quo_rem(self, name, a, b, exp_quo, exp_rem):
        (quo, rem) = quo_rem(a, b)
        self.assertEqual((quo,rem), (exp_quo, exp_rem))

    @parameterized.expand([
        ['1', [5, 5, 5, 5], [7, 7, 7, 7], [1, 3, 3, 3, 2]],
        ['2', [9, 9, 9, 9], [7, 7, 7], [1, 0, 7, 7, 6]]

    ])
    def test_add(self, name,  a, b, e):
        self.assertTrue((add(a, b) == e).all())

    @parameterized.expand([
        ['1', [2,2], [3,3], [7, 2, 6]]

    ])
    def test_mul(self, name, a, b, e):
        self.assertTrue((mul(a, b) == e).all())
