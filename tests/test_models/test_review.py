#!/usr/bin/python3
"""This module has unittest"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class represets the tests for place"""
    def setUp(self):
        """This is the setUp method for the tests"""
        self.review = Review(
                place_id="123", user_id="321", text="string of text")

    def test_review_attributes(self):
        """This method tests the attribures"""
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "321")
        self.assertEqual(self.review.text, "string of text")

    def test_review_type(self):
        """This method tests for attribute types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_inheritance(self):
        """Thsi method tests for attribute inheritance logic"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)


if __name__ == '__main__':
    unittest.main()
