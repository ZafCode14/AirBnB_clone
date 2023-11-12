#!/usr/bin/python3
"""Module with a unittest for storage"""
import os
import unittest
import pep8
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestStorage(unittest.TestCase):
    """Class that represents the tests for model"""
    def setUp(self):
        """Method that sets up"""
        self.classes = [
                "BaseModel", "User", "Place",
                "State", "City", "Amenity", "Review"]

    def tearDown(self) -> None:
        """Resets FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_style(self):
        """Test for style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

    def test_all(self):
        """Test for the all method"""
        self.assertEqual(dict, type(storage.all()))

        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """Test for the new method with all classes"""
        for cls in self.classes:
            obj = globals()[cls]()
            storage.new(obj)
            self.assertIn("{}.{}".format(cls, obj.id), storage.all().keys())

            with self.assertRaises(TypeError):
                storage.new(obj, 1)

    def test_save(self):
        """Test for the save mthod with all classes"""
        for cls in self.classes:
            obj = globals()[cls]()
            storage.new(obj)
            storage.save()
            saved_txt = ""
            with open("file.json", "r") as f:
                saved_txt = f.read()
                self.assertIn("{}.{}".format(cls, obj.id), saved_txt)
            with self.assertRaises(TypeError):
                storage.save(None)

    def test_reload(self):
        """Test for the reload method with all classes"""
        for cls in self.classes:
            obj = globals()[cls]()
            storage.new(obj)
            storage.save()
            storage.reload()
            objs = FileStorage._FileStorage__objects
            self.assertIn("{}.{}".format(cls, obj.id), objs)

            with self.assertRaises(TypeError):
                storage.reload(None)

    def test_save_reload_new(self):
        """Test the reload method"""
        for cls in self.classes:
            obj = globals()[cls]()
            obj.name = "Alice"
            storage.new(obj)
            storage.save()
            storage.reload()
            loaded_data = storage.all()

            self.assertIn("{}.{}".format(cls, obj.id), loaded_data)
            loaded_obj = loaded_data["{}.{}".format(cls, obj.id)]
            self.assertEqual(loaded_obj.name, "Alice")


if __name__ == "__main__":
    unittest.main()
