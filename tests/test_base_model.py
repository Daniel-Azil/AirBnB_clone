#!/usr/bin/python3

"""
    A module that test cases for the BaseModel class
    from models/base_model.py
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
        A class that test cases for the BaseModel class.
    """

    def test_base_model_creation(self):
        """
            A method that test creating a BaseModel instance.
        """
        self.base_model = BaseModel()
        self.assertIsInstance(self.base_model, BaseModel)

    def test_base_model_id(self):
        """
            A method that test the 'id' attribute of BaseModel.
        """
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertNotEqual(self.base_model.id, "")

    def test_base_model_created_at(self):
        """
            A method that test the 'created_at' attribute of BaseModel.
        """
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_base_model_updated_at(self):
        """
            A method that test the 'updated_at' attribute of BaseModel.
        """
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_base_model_to_dict(self):
        """
            A method that test the to_dict method of BaseModel.
        """
        self.base_model = BaseModel()
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)

        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        for key in expected_keys:
            self.assertIn(key, base_model_dict)

    def test_base_model_str(self):
        """
            A method that test the __str__ method of BaseModel.
        """
        self.base_model = BaseModel()
        base_model_str = str(self.base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertIn(self.base_model.__class__.__name__, base_model_str)
        self.assertIn(str(self.base_model.id), base_model_str)

    def test_base_model_repr(self):
        """
            A method that test the __repr__ method of BaseModel.
        """
        self.base_model = BaseModel()
        base_model_repr = repr(self.base_model)
        self.assertIsInstance(base_model_repr, str)
        self.assertIn(self.base_model.__class__.__name__, base_model_repr)
        self.assertIn(str(self.base_model.id), base_model_repr)


if __name__ == '__main__':
    unittest.main()
