#!/usr/bin/env python3
"""

    Contains the entry point of the command interpreter

"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, line: str) -> True:
        """ Quit command to exit the program. """
        return True

    def emptyline(self) -> bool:
        return False

    def do_create(self, line) -> None:
        """ Creates instance save it to the JSON file """
        lst_cls = (["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"])
        if line == "":
            print("** class name missing **")
        elif line in lst_cls:
            new_instance = globals()[line]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line) -> None:
        """ Prints the string representation of an instance """
        flag = False
        lst_cls = (["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"])
        command_list = line.split()
        if line == "" and len(command_list) == 0:
            print("** class name missing **")
        elif len(command_list) == 1 and command_list[0] not in lst_cls:
            print("** class doesn't exist **")
        elif len(command_list) == 2 and command_list[0] in lst_cls:
            key_join = ".".join(command_list)
            for k, v in models.storage.all().items():
                if k == key_join:
                    print(v)
                    flag = True
            if not flag:
                print("** no instance found **")
        elif len(command_list) < 2:
            print("** instance id missing **")

    def do_destroy(self, line) -> None:
        """ Deletes an instance based on the class name and id """
        flag = True
        lst_command = line.split()
        cls_lst = (["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"])
        if line == "" and len(lst_command) == 0:
            print("** class name missing **")
        elif len(lst_command) == 1 and lst_command[0] not in cls_lst:
            print("** class doesn't exist **")
        elif len(lst_command) < 2:
            print("** instance id missing **")
        elif len(lst_command) == 2:
            str_command = ".".join(lst_command)
            if str_command in models.storage.all().keys():
                del models.storage.all()[str_command]
            else:
                print("** no instance found **")

    def do_all(self, line) -> None:
        """ Prints all string representation of all instances """
        str_lst = []
        line_arg = line.split()
        cls_lst = (["BaseModel", "User", "Place",
                    "State", "City", "Amenity", "Review"])
        if not line_arg:
            for obj in models.storage.all().values():
                str_lst.append(str(obj))
            print(str_lst)
        elif line_arg[0] in cls_lst:
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == line_arg[0]:
                    str_lst.append(str(obj))
            print(str_lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
            """Updates an instance based on the class name and id."""
            args = []
            in_quotes = False
            current_arg = ""
            cls_lst = (["BaseModel", "User", "Place",
                        "State", "City", "Amenity", "Review"])

            for char in line:
                if char == ' ' and not in_quotes:
                    args.append(current_arg)
                    current_arg = ""
                elif char == '"':
                    in_quotes = not in_quotes
                else:
                    current_arg += char

            if current_arg:
                args.append(current_arg)

            if len(args) < 1:
                print("* class name missing *")
            elif not args[0] in cls_lst:
                return
            elif len(args) < 2:
                print("* instance id missing *")
            elif len(args) < 3:
                print("* attribute name missing *")
            elif len(args) < 4:
                print("* value missing *")
            else:
                obj_key = "{}.{}".format(args[0], args[1])
                if obj_key in models.storage.all():
                    instance = models.storage.all()[obj_key]
                    attribute_name = args[2]
                    value = args[3]
                    setattr(instance, attribute_name, value)
                    models.storage.save()
                else:
                    print("* no instance found *")
    # Aliasing
    do_EOF = do_quit


if __name__ == '__main__':

    HBNBCommand().cmdloop()
