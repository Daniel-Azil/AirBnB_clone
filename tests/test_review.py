#!/usr/bin/python3

"""
A module that contains test cases for the Review class from models/review.py
"""

import unittest
from models.review import Review
from datetime import datetime
import uuid


class TestReview(unittest.TestCase):
    """
    A class that contains test cases for the Review class.
    """

    def test_review_creation(self):
        """
        A method that tests creating a Review instance.
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_id(self):
        """
        A method that tests the 'id' attribute of Review.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertIsInstance(review.id, str)
        self.assertNotEqual(review.id, "")

    def test_review_created_at(self):
        """
        A method that tests the 'created_at' attribute of Review.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertIsInstance(review.created_at, datetime)

    def test_review_updated_at(self):
        """
        A method that tests the 'updated_at' attribute of Review.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertIsInstance(review.updated_at, datetime)

    def test_review_to_dict(self):
        """
        A method that tests the to_dict method of Review.
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)

        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        for key in expected_keys:
            self.assertIn(key, review_dict)

    def test_review_str(self):
        """
        A method that tests the __str__ method of Review.
        """
        review = Review()
        review_str = str(review)
        self.assertIsInstance(review_str, str)
        self.assertIn(review.__class__.__name__, review_str)
        self.assertIn(str(review.id), review_str)

    def test_review_repr(self):
        """
        A method that tests the __repr__ method of Review.
        """
        review = Review()
        review_repr = repr(review)
        self.assertIsInstance(review_repr, str)
        self.assertIn(review.__class__.__name__, review_repr)
        self.assertIn(str(review.id), review_repr)


if __name__ == '__main__':
    unittest.main()
