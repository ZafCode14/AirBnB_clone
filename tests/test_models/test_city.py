#!/usr/bin/python3
"""This module has unittest"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class represets the tests for city"""
    def setUp(self):
        """This is the setUp method for the tests"""
        self.city = City(state_id="123", name="London")

    def test_city_attributes(self):
        """This method tests the attribures"""
        self.assertEqual(self.city.state_id, "123")
        self.assertEqual(self.city.name, "London")

    def test_city_type(self):
        """This method tests for attribute types"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inheritance(self):
        """Thsi method tests for attribute inheritance logic"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)


if __name__ == '__main__':
    unittest.main()
