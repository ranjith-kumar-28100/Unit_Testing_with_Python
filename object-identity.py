import unittest


class IdentityTests(unittest.TestCase):
    def test_indenticality(self):
        a = [1, 2, 3]
        c = [1, 2, 3]
        b = a
        self.assertIs(a, b)
        self.assertIsNot(a, c)
        self.assertIsNot(b, c)


if __name__ == "__main__":
    unittest.main()
