#!/usr/bin/python3
"""Module with a unittest"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import json


class TestConsole(unittest.TestCase):
    """Class with console tests"""

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_basic_commands(self):
        """Tests basic commands."""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(),
                    "Creates a new instance of a class, \
saves it, and prints the id.\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? all")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(),
                    "Prints all string representations of instances.\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? show")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(),
                    'Prints the string representation of an instance.\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? update")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(),
                    'Updates an instance based on the class name and id.\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? destroy")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(), 'Deletes an instance based \
on the class name and id.\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? quit")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(),
                    "Quits the program\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? help")
            self.assertIsInstance(f.getvalue(), str)
            self.assertEqual(
                    f.getvalue(), 'List available commands with \
"help" or detailed help with "help cmd".\n')


class TestCommands(unittest.TestCase):
    """Testing commands."""

    def setUp(self):
        self.classes = [
                "BaseModel", "User", "Place",
                "State", "City", "Amenity", "Review"]

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_create_basemodel(self):
        """test 'create' with all basemodel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("BaseModel.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_create_user(self):
        """test 'create' with all user"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("User.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_create_state(self):
        """test 'create' with all state"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("State.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_create_city(self):
        """test 'create' with all city"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("City.{}".format(
                f.getvalue().strip()), storage.all().keys())
                
    def test_create_amenity(self):
        """test 'create' with all amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("Amenity.{}".format(
                f.getvalue().strip()), storage.all().keys())
                
    def test_create_place(self):
        """test 'create' with all place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("Place.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_create_review(self):
        """test 'create' with all review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            self.assertIsInstance(f.getvalue(), str)
            self.assertIn("Review.{}".format(
                f.getvalue().strip()), storage.all().keys())

    def test_all_BaseModel(self):
        """Tests 'all' with BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[BaseModel]")

    def test_all_User(self):
        """Tests 'all' with User"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[User]")

    def test_all_City(self):
        """Tests 'all' with City"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[City]")

    def test_all_Amenity(self):
        """Tests 'all' with Amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[Amenity]")
                
    def test_all_Place(self):
        """Tests 'all' with Place"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[Place]")
                
    def test_all_Review(self):
        """Tests 'all' with Review"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
            for item in json.loads(f.getvalue()):
                self.assertEqual(item.split()[0], "[Review]")

    def test_show_BaseModel(self):
        """Test 'show' with BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = BaseModel()
            instance.name = "Mike"
            HBNBCommand().onecmd("show BaseModel {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[BaseModel] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_show_User(self):
        """Test 'show' with User"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = User()
            instance.name = "Mike"
            HBNBCommand().onecmd("show User {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[User] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_show_State(self):
        """Test 'show' with State"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = State()
            instance.name = "Mike"
            HBNBCommand().onecmd("show State {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[State] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_show_City(self):
        """Test 'show' with City"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = City()
            instance.name = "Mike"
            HBNBCommand().onecmd("show City {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[City] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_show_Amenity(self):
        """Test 'show' with Amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Amenity()
            instance.name = "Mike"
            HBNBCommand().onecmd("show Amenity {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[Amenity] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_show_Place(self):
        """Test 'show' with Place"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Place()
            instance.name = "Mike"
            HBNBCommand().onecmd("show Place {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[Place] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_show_Review(self):
        """Test 'show' with Review"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Review()
            instance.name = "Mike"
            HBNBCommand().onecmd("show Review {}".format(instance.id))
            self.assertEqual(
                    f.getvalue().strip(),
                    "[Review] ({}) {}".format(
                        instance.id, instance.__dict__))

    def test_destroy_BaseModel(self):
        """Test 'destroy' with BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = BaseModel()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy BaseModel {}".format(
                instance.id))
            self.assertNotIn(
                    "BaseModel.{}".format(instance.id), storage.all().keys())

    def test_destroy_User(self):
        """Test 'destroy' with User"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = User()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy User {}".format(
                instance.id))
            self.assertNotIn(
                    "User.{}".format(instance.id), storage.all().keys())

    def test_destroy_State(self):
        """Test 'destroy' with State"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = State()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy State {}".format(
                instance.id))
            self.assertNotIn(
                    "State.{}".format(instance.id), storage.all().keys())

    def test_destroy_City(self):
        """Test 'destroy' with City"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = City()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy City {}".format(
                instance.id))
            self.assertNotIn(
                    "City.{}".format(instance.id), storage.all().keys())

    def test_destroy_Amenity(self):
        """Test 'destroy' with Amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Amenity()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy Amenity {}".format(
                instance.id))
            self.assertNotIn(
                    "Amenity.{}".format(instance.id), storage.all().keys())

    def test_destroy_Place(self):
        """Test 'destroy' with Place"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Place()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy Place {}".format(
                instance.id))
            self.assertNotIn(
                    "Place.{}".format(instance.id), storage.all().keys())

    def test_destroy_Review(self):
        """Test 'destroy' with Review"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Review()
            instance.name = "Mike"
            HBNBCommand().onecmd("destroy Review {}".format(
                instance.id))
            self.assertNotIn(
                    "Review.{}".format(instance.id), storage.all().keys())

    def test_update_BaseModel(self):
        """Test 'update' with BaseModel"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = BaseModel()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update BaseModel {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update BaseModel {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update BaseModel {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update BaseModel {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update BaseModel {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))
            
    def test_update_User(self):
        """Test 'update' with User"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = User()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update User {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update User {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update User {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update User {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update User {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))

    def test_update_State(self):
        """Test 'update' with State"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = State()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update State {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update State {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update State {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update State {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update State {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))

    def test_update_City(self):
        """Test 'update' with City"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = City()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update City {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update City {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update City {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update City {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update City {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))

    def test_update_Amenity(self):
        """Test 'update' with Amenity"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Amenity()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update Amenity {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update Amenity {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update Amenity {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update Amenity {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update Amenity {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))

    def test_update_Place(self):
        """Test 'update' with Place"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Place()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update Place {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update Place {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update Place {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update Place {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update Place {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))

    def test_update_Review(self):
        """Test 'update' with Review"""
        with patch('sys.stdout', new=StringIO()) as f:
            instance = Review()
            instance.name = "Halper"
            instance.age = 23
            instance.height = 1.98
            HBNBCommand().onecmd(
                    'update Review {} name "Peterson"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update Review {} age 87'.format(instance.id))
            HBNBCommand().onecmd(
                    'update Review {} height 1.65'.format(instance.id))
            HBNBCommand().onecmd(
                    'update Review {} description "Happy, lovely"'.format(
                        instance.id))
            HBNBCommand().onecmd(
                    'update Review {} pet "dog" dog_name "Rex"'.format(
                        instance.id))
            self.assertEqual(instance.__dict__["name"], "Peterson")
            self.assertEqual(instance.__dict__["age"], "87")
            self.assertEqual(instance.__dict__["height"], "1.65")
            self.assertEqual(
                    instance.__dict__["description"], "Happy, lovely")
            self.assertEqual(instance.__dict__["pet"], "dog")
            self.assertNotIn("dog_name", dir(instance))
'''
class TestCommandsDot(unittest.TestCase):
    """Testing commands."""

    def setUp(self):
        self.classes = [
                "BaseModel", "User", "review",
                "State", "City", "Amenity", "Review"]

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_all(self):
        """Tests 'all' with all classes"""
        for cls in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(
                        HBNBCommand().precmd("{}.all()".format(cls)))
                for item in json.loads(f.getvalue()):
                    self.assertEqual(item.split()[0], "[{}]".format(cls))

    def test_show(self):
        """Test 'show' with all classes"""
        for cls in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                instance = globals()[cls]()
                instance.name = "Mike"
                HBNBCommand().onecmd(
                        HBNBCommand().precmd(
                            '{}.show("{}")'.format(cls, instance.id)))
                self.assertEqual(
                        f.getvalue().strip(),
                        "[{}] ({}) {}".format(
                            cls, instance.id, instance.__dict__))

    def test_destroy(self):
        """Test 'destroy' with all classes"""
        for cls in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                instance = globals()[cls]()
                instance.name = "Mike"
                HBNBCommand().onecmd(
                        HBNBCommand().precmd(
                            '{}.destroy("{}")'.format(cls, instance.id)))
                self.assertNotIn(
                        "{}.{}".format(cls, instance.id), storage.all().keys())

    def test_update(self):
        """Test 'update' with all classes"""
        for cls in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                instance = globals()[cls]()
                instance.name = "Halper"
                instance.age = 23
                instance.height = 1.98
                HBNBCommand().onecmd(
                        HBNBCommand().precmd(
                            '{}.update("{}", "name", "Barter")'.format(
                                cls, instance.id)))
                HBNBCommand().onecmd(
                        HBNBCommand().precmd(
                            '{}.update("{}", "age", "2")'.format(
                                cls, instance.id)))
                HBNBCommand().onecmd(
                        HBNBCommand().precmd(
                            '{}.update("{}", "height", "0.6")'.format(
                                cls, instance.id)))
                HBNBCommand().onecmd(
                        HBNBCommand().precmd(
                            '{}.update("{}", "description", "What a nice day")'
                            .format(cls, instance.id)))
                self.assertEqual(instance.__dict__["name"], "Barter")
                self.assertEqual(instance.__dict__["age"], "2")
                self.assertEqual(instance.__dict__["height"], "0.6")
                self.assertEqual(
                        instance.__dict__["description"], "What a nice day")

    def test_count(self):
        """Tests 'count' with all classes"""
        for cls in self.classes:
            instance = globals()[cls]()
            instance = globals()[cls]()
            instance = globals()[cls]()
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(
                        HBNBCommand().precmd("{}.count()".format(cls)))
                count = 0
                for i in storage.all().values():
                    if type(i) == BaseModel:
                        count += 1
                self.assertEqual(int(f.getvalue()), count)
'''


if __name__ == '__main__':
    unittest.main()
