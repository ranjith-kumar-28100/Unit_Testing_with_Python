import unittest


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("y should never be 0")
    return x / y


class TestErrors(unittest.TestCase):
    def test_divide1(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_divide2(self):
        with self.assertRaises(ZeroDivisionError):
            divide(100, 0)


if __name__ == "__main__":
    unittest.main()
