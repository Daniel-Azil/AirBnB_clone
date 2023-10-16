#!/usr/bin/python3

""" A module that checks the test cases for city class"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    A class that contains test cases for the City class.
    """

    def test_city_creation(self):
        """
        A method that tests creating a City instance.
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_state_id(self):
        """
        A method that tests the 'state_id' attribute of the City class.
        """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertIsInstance(city.state_id, str)
        self.assertEqual(city.state_id, "")

    def test_city_name(self):
        """
        A method that tests the 'name' attribute of the City class.
        """
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertIsInstance(city.name, str)
        self.assertEqual(city.name, "")

    def test_city_inherits_from_base_model(self):
        """
        A method that tests if City inherits from BaseModel.
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_city_created_at(self):
        """
        A method that tests the 'created_at' attribute of the City class.
        """
        city = City()
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_at(self):
        """
        A method that tests the 'updated_at' attribute of the City class.
        """
        city = City()
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_to_dict(self):
        """
        A method that tests the to_dict method of the City class.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)

        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        for key in expected_keys:
            self.assertIn(key, city_dict)

    def test_city_str(self):
        """
        A method that tests the __str__ method of the City class.
        """
        city = City()
        city_str = str(city)
        self.assertIsInstance(city_str, str)
        self.assertIn(city.__class__.__name__, city_str)
        self.assertIn(str(city.id), city_str)

    def test_city_repr(self):
        """
        A method that tests the __repr__ method of the City class.
        """
        city = City()
        city_repr = repr(city)
        self.assertIsInstance(city_repr, str)
        self.assertIn(city.__class__.__name__, city_repr)
        self.assertIn(str(city.id), city_repr)


if __name__ == '__main__':
    unittest.main()
