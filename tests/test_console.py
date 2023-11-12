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

    def test_create(self):
        """Test 'create' with all classes"""
        for cls in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertIn("{}.{}".format(
                    cls, f.getvalue().strip()), storage.all().keys())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class name missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create xxx")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class doesn't exist **", f.getvalue().strip())

    def test_all(self):
        """Tests 'all' with all classes"""
        for cls in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all {}".format(cls))
                for item in json.loads(f.getvalue()):
                    self.assertEqual(item.split()[0], "[{}]".format(cls))
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all xxx")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class doesn't exist **", f.getvalue().strip())

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
                HBNBCommand().onecmd("show {} {}".format(cls, instance.id))
                self.assertEqual(
                        f.getvalue().strip(),
                        "[{}] ({}) {}".format(
                            cls, instance.id, instance.__dict__))
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class name missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show xxx")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class doesn't exist **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {}".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** instance id missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} 111".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** no instance found **", f.getvalue().strip())

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
                HBNBCommand().onecmd("destroy {} {}".format(cls, instance.id))
                self.assertNotIn(
                        "{}.{}".format(cls, instance.id), storage.all().keys())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class name missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy xxx")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class doesn't exist **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {}".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** instance id missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {} 111".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** no instance found **", f.getvalue().strip())

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
                        'update {} {} name "Peterson"'.format(
                            cls, instance.id))
                HBNBCommand().onecmd(
                        'update {} {} age 87'.format(cls, instance.id))
                HBNBCommand().onecmd(
                        'update {} {} height 1.65'.format(cls, instance.id))
                HBNBCommand().onecmd(
                        'update {} {} description "Happy, lovely"'.format(
                            cls, instance.id))
                HBNBCommand().onecmd(
                        'update {} {} pet "dog" dog_name "Rex"'.format(
                            cls, instance.id))
                self.assertEqual(instance.__dict__["name"], "Peterson")
                self.assertEqual(instance.__dict__["age"], "87")
                self.assertEqual(instance.__dict__["height"], "1.65")
                self.assertEqual(
                        instance.__dict__["description"], "Happy, lovely")
                self.assertEqual(instance.__dict__["pet"], "dog")
                self.assertNotIn("dog_name", dir(instance))
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class name missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update xxx")
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** class doesn't exist **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {}".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** instance id missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {} 111".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** attribute name missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {} 111 first_name".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** value missing **", f.getvalue().strip())
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(
                        "update {} 111 first_name John".format(cls))
                self.assertIsInstance(f.getvalue(), str)
                self.assertEqual(
                        "** no instance found **", f.getvalue().strip())

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


if __name__ == '__main__':
    unittest.main()
