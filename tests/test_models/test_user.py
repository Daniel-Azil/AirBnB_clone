#!/usr/bin/python3

""" A module that checks the test clases for user class"""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    A class that contains test cases for the User class.
    """

    def test_user_creation(self):
        """
        A method that tests creating a User instance.
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_user_email(self):
        """
        A method that tests the 'email' attribute of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertIsInstance(user.email, str)
        self.assertEqual(user.email, "")

    def test_user_password(self):
        """
        A method that tests the 'password' attribute of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertIsInstance(user.password, str)
        self.assertEqual(user.password, "")

    def test_user_first_name(self):
        """
        A method that tests the 'first_name' attribute of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertIsInstance(user.first_name, str)
        self.assertEqual(user.first_name, "")

    def test_user_last_name(self):
        """
        A method that tests the 'last_name' attribute of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertIsInstance(user.last_name, str)
        self.assertEqual(user.last_name, "")

    def test_user_inherits_from_base_model(self):
        """
        A method that tests if User inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_user_created_at(self):
        """
        A method that tests the 'created_at' attribute of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertIsInstance(user.created_at, datetime)

    def test_user_updated_at(self):
        """
        A method that tests the 'updated_at' attribute of the User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_to_dict(self):
        """
        A method that tests the to_dict method of the User class.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)

        expected_keys = ['__class__', 'id', 'created_at',
                         'updated_at']
        for key in expected_keys:
            self.assertIn(key, user_dict)

    def test_user_str(self):
        """
        A method that tests the __str__ method of the User class.
        """
        user = User()
        user_str = str(user)
        self.assertIsInstance(user_str, str)
        self.assertIn(user.__class__.__name__, user_str)
        self.assertIn(str(user.id), user_str)

    def test_user_repr(self):
        """
        A method that tests the __repr__ method of the User class.
        """
        user = User()
        user_repr = repr(user)
        self.assertIsInstance(user_repr, str)
        self.assertIn(user.__class__.__name__, user_repr)
        self.assertIn(str(user.id), user_repr)


if __name__ == '__main__':
    unittest.main()
