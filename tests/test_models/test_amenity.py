#!/usr/bin/python3
"""This module has unittest"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class represets the tests for amenity"""
    def setUp(self):
        """This is the setUp method for the tests"""
        self.amenity = Amenity(name="amenity")

    def test_amenity_attributes(self):
        """This method tests the attribures"""
        self.assertEqual(self.amenity.name, "amenity")

    def test_amenity_type(self):
        """This method tests for attribute types"""
        self.assertIsInstance(self.amenity.name, str)

    def test_inheritance(self):
        """Thsi method tests for attribute inheritance logic"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
