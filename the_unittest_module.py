import unittest


class TestStringMethods(unittest.TestCase):
    def test_split(self):
        self.assertEqual("a-b-c".split("-"), ["a", "b", "c"])
        self.assertEqual("a+b+c".split("+"), ["a", "b", "c"])

    def test_count(self):
        self.assertEqual("tata is the tata".count("t"), 5)
        self.assertEqual("".count("t"), 0)


if __name__ == "__main__":
    unittest.main()
