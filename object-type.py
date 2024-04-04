import unittest


class Vehicle:
    def __init__(self):
        self.wheels = 4
        self.type = "Disel"
        self.name = "Lorry"


class Bird:
    def __init__(self):
        self.legs = 2
        self.wings = 2
        self.name = "Parrot"


class Peacock(Bird):
    def __init__(self):
        super().__init__()
        self.name = "Peacock"
        self.speciality = "Dancing"


class TestObjectType(unittest.TestCase):
    def test_isinstance(self):
        lorry = Vehicle()
        parrot = Bird()
        peacock = Peacock()
        self.assertIsInstance(lorry, Vehicle)
        self.assertIsInstance(parrot, Bird)
        self.assertIsInstance(peacock, Peacock)
        self.assertIsInstance(peacock, Bird)

    def test_notinstance(self):
        lorry = Vehicle()
        parrot = Bird()
        peacock = Peacock()
        self.assertNotIsInstance(lorry, Bird)
        self.assertNotIsInstance(parrot, Peacock)
        self.assertNotIsInstance(peacock, Vehicle)


if __name__ == "__main__":
    unittest.main()
