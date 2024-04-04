import unittest


class TestOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will run once before first testcase starts.")

    def setUp(self):
        print("This will run before each test.")

    def test_case1(self):
        self.assertEqual(88 // 88, 1)

    def test_case2(self):
        self.assertEqual([] == (), False)

    def tearDown(self):
        print("This will run after each test.")

    @classmethod
    def tearDownClass(cls):
        print("This will run once after last testcase ends.")


if __name__ == "__main__":
    unittest.main()
