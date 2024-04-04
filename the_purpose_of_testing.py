def multiply(a, b):
    prod = 0
    if a == 0 or b == 0:
        return prod
    if isinstance(a, float) or isinstance(b, float):
        return round(a * b, 2)
    for _ in range(abs(a)):
        prod += abs(b)
    if a < 0 and b < 0:
        return prod
    if a < 0 or b < 0:
        return -prod
    return prod


import unittest


class TestMultiplyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_case_2(self):
        self.assertEqual(multiply(0, 6), 0)

    def test_case_3(self):
        self.assertEqual(multiply(-1, -6), 6)

    def test_case4(self):
        self.assertEqual(multiply(-9, 6), -54)

    def test_case5(self):
        self.assertEqual(multiply(10000, 566), 5660000)

    def test_case6(self):
        self.assertEqual(multiply(0.1, 0.1), 0.01)


if __name__ == "__main__":
    unittest.main()
