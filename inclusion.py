import unittest


class InclusionTest(unittest.TestCase):
    def test_isin(self):
        self.assertIn("k", "king")
        self.assertIn("name", {"name": "rkg", "age": 24})
        self.assertIn(24, {"name": "rkg", "age": 24}.values())
        self.assertIn(5, range(500))

    def test_notin(self):
        self.assertNotIn("R", "king")
        self.assertNotIn("R", list("king"))


if __name__ == "__main__":
    unittest.main()
