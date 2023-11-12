#!/usr/bin/python3
"""This module has unittest"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class represets the tests for state"""
    def setUp(self):
        """This is the setUp method for the tests"""
        self.state = State(name="California")

    def test_state_attributes(self):
        """This method tests the attribures"""
        self.assertEqual(self.state.name, "California")

    def test_attributes_type(self):
        """This method tests for attribute types"""
        self.assertIsInstance(self.state.name, str)

    def test_inheritance(self):
        """Thsi method tests for attribute inheritance logic"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)


if __name__ == '__main__':
    unittest.main()
