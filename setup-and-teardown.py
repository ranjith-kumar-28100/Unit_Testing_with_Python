import unittest


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state


class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Restaurant:
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def get_owners_age(self):
        return self.owner.age

    def summary(self):
        return f"This restaurant is owned by {self.owner.name} and is located in {self.address.city}."


import unittest


class TestRestaurant(unittest.TestCase):
    def setUp(self):
        print("This will run before each test!")
        self.address = Address(city="Bengaluru", state="Karnataka")
        self.owner = Owner(name="Ranjith Kumar", age=24)
        self.my_restaurant = Restaurant(address=self.address, owner=self.owner)

    def tearDown(self):
        print("This will run after each test!")

    def test_owner_age(self):
        self.assertEqual(self.my_restaurant.get_owners_age, 24)

    def test_summary(self):
        self.assertEqual(
            self.my_restaurant.summary(),
            "This restaurant is owned by Ranjith Kumar and is located in Bengaluru.",
        )


if __name__ == "__main__":
    unittest.main()
