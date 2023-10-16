#!/usr/bin/python3

"""
    A module test cases for the Place class from
    models/place.py
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
        A class test cases for the Place class.
    """

    def test_place_creation(self):
        """
        A method that test creating a Place instance.
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """
            A method that test setting and getting
            attributes of the Place class.
        """
        place = Place()
        place.city_id = "City123"
        place.user_id = "User456"
        place.name = "Cozy Cabin"
        place.description = "A beautiful cabin in the woods"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 42.123456
        place.longitude = -72.654321
        place.amenity_ids = ["pool", "wifi", "kitchen"]

        self.assertEqual(place.city_id, "City123")
        self.assertEqual(place.user_id, "User456")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.description, "A beautiful cabin in the woods")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 42.123456)
        self.assertEqual(place.longitude, -72.654321)
        self.assertEqual(place.amenity_ids, ["pool", "wifi", "kitchen"])


if __name__ == '__main__':
    unittest.main()
