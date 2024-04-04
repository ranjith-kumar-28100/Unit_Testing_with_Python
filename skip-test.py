import unittest


class TestSkipTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(1 - 1, 0)

    @unittest.skip("To be implemented later")
    def test_multiplication(self):
        pass


if __name__ == "__main__":
    unittest.main()
