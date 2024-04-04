import unittest


def implicit_show_message():
    print("Hello World")


def explicit_show_message():
    return "Hello World"


class Test_nullness(unittest.TestCase):
    def test_none(self):
        self.assertIsNone(implicit_show_message())

    def test_not_none(self):
        self.assertIsNotNone(explicit_show_message())


if __name__ == "__main__":
    unittest.main()
