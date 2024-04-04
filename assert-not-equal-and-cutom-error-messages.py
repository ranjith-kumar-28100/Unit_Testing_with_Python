import unittest


def copy_and_add_element(values, element):
    copy = values[:]
    copy.append(element)
    return copy


class TestInEquality(unittest.TestCase):
    def test_case1(self):
        self.assertNotEqual(1, 2)

    def test_case2(self):
        self.assertEqual(
            "S-T-R".split("-"),
            [],
            "Split never returns empty list for non-empty strings",
        )

    def test_copy_and_add_element(self):
        input = [1, 2, 3]
        output = copy_and_add_element(input, 4)
        self.assertEqual(output, [1, 2, 3, 4])
        self.assertNotEqual(
            input,
            [1, 2, 3, 4],
            "Original list is been mutated, ensure copy is been created and operated on",
        )


if __name__ == "__main__":
    unittest.main()
