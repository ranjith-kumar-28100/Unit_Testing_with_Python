import unittest


class Test_Truthiness_Falsiness(unittest.TestCase):
    def test_truthiness(self):
        self.assertTrue([1, 2, 3])
        self.assertTrue("Hello")
        self.assertTrue(-6556)
        self.assertTrue([1, 2, 3] != (1, 2, 3))

    def test_falsiness(self):
        self.assertFalse("")
        self.assertFalse(0)
        self.assertFalse([])
        self.assertFalse([] == ())


if __name__ == "__main__":
    unittest.main()
