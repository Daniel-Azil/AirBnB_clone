#!/usr/bin/python3
"""
    A unittest case module for amenity module
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
        A test case class for amenity module functionality
    """

    def test_amenity_creation(self):
        """ Method test creating an Amenity instance """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name(self):
        """ Metthod test case for amenity """
        amenity = Amenity()
        amenity.name = "Parking lot"
        self.assertEqual(amenity.name, "Parking lot")


if __name__ == '__main__':
    unittest.main()
