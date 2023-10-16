#!/usr/bin/python3

""" A module that checks the test cases for State class """

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    A class that contains test cases for the State class.
    """

    def test_state_creation(self):
        """
        A method that tests creating a State instance.
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name(self):
        """
        A method that tests the 'name' attribute of the State class.
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "")

    def test_state_inherits_from_base_model(self):
        """
        A method that tests if State inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_created_at(self):
        """
        A method that tests the 'created_at' attribute of the State class.
        """
        state = State()
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertIsInstance(state.created_at, datetime)

    def test_state_updated_at(self):
        """
        A method that tests the 'updated_at' attribute of the State class.
        """
        state = State()
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_to_dict(self):
        """
        A method that tests the to_dict method of the State class.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)

        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        for key in expected_keys:
            self.assertIn(key, state_dict)

    def test_state_str(self):
        """
        A method that tests the __str__ method of the State class.
        """
        state = State()
        state_str = str(state)
        self.assertIsInstance(state_str, str)
        self.assertIn(state.__class__.__name__, state_str)
        self.assertIn(str(state.id), state_str)

    def test_state_repr(self):
        """
        A method that tests the __repr__ method of the State class.
        """
        state = State()
        state_repr = repr(state)
        self.assertIsInstance(state_repr, str)
        self.assertIn(state.__class__.__name__, state_repr)
        self.assertIn(str(state.id), state_repr)


if __name__ == '__main__':
    unittest.main()
