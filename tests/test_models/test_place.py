#!/usr/bin/python3
"""Module with a unittest"""
import unittest
import os
import pep8
from datetime import datetime
from models.place import Place
from models import storage
from models.engine.file_storage import FileStorage
import json


class TestUser(unittest.TestCase):
    """Class that represents the tests for model"""
    def tearDown(self) -> None:
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_style(self):
        """Test style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_init(self):
        """test initializing method"""
        obj = Place()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        """Test the string method"""
        obj = Place()
        expected_str = "[Place] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        """Test the save method"""
        obj = Place()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """Test the dict method"""
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())
        self.assertEqual(obj_dict["__class__"], "Place")

    def test_to_dict_with_custom_attributes(self):
        """Test the dict method with custom attributes"""
        obj = Place()
        obj.name = "Alice"
        obj.age = 30
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict["name"], "Alice")
        self.assertEqual(obj_dict["age"], 30)

    def test_init_with_kwargs(self):
        """Test init with a dictionary passed"""
        data = {
            "id": "12345",
            "created_at": "2023-11-07T12:34:56.789012",
            "updated_at": "2023-11-08T01:23:45.678901",
            "custom_attr": "value"
        }
        obj = Place(**data)
        self.assertEqual(obj.id, "12345")
        self.assertEqual(
                obj.created_at.isoformat(), "2023-11-07T12:34:56.789012")
        self.assertEqual(
                obj.updated_at.isoformat(), "2023-11-08T01:23:45.678901")
        self.assertEqual(obj.custom_attr, "value")


if __name__ == "__main__":
    unittest.main()
