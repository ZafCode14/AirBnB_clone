#!/usr/bin/python3
"""This module has unittest"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """This class represets the tests for place"""
    def setUp(self):
        """This is the setUp method for the tests"""
        self.place = Place(
                city_id="123", user_id="321", name="place name",
                description="place description", number_rooms=1,
                number_bathrooms=1, max_guest=1, price_by_night=20,
                latitude=23.23, longitude=52.50, amenity_ids="amenity_ids")

    def test_place_attributes(self):
        """This method tests the attribures"""
        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "321")
        self.assertEqual(self.place.name, "place name")
        self.assertEqual(self.place.description, "place description")
        self.assertEqual(self.place.number_rooms, 1)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 1)
        self.assertEqual(self.place.price_by_night, 20)
        self.assertEqual(self.place.latitude, 23.23)
        self.assertEqual(self.place.longitude, 52.50)
        self.assertEqual(self.place.amenity_ids, "amenity_ids")

    def test_place_type(self):
        """This method tests for attribute types"""
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, str)

    def test_inheritance(self):
        """Thsi method tests for attribute inheritance logic"""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)


if __name__ == '__main__':
    unittest.main()
