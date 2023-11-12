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
        """ Creates instance of BaseModel, saves it to the JSON file """
        lst_cls = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
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
        lst_cls = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
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
        cls_lst = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
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
        cls_lst = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
        if line == "":
            for obj in models.storage.all().values():
                str_lst.append(obj.__str__())
            print(str_lst)
        elif line not in cls_lst:
            print("** class doesn't exist **")

    def do_update(self, line) -> None:
        """ Updates an instance by adding or updating attribute """
        flag = False
        words_lst = line.split()
        cls_lst = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
        if len(words_lst) >= 2:
            key_word = "{}.{}".format(words_lst[0], words_lst[1])
            for k in models.storage.all().keys():
                if k == key_word:
                    flag = True
        if len(words_lst) == 0:
            print("** class name missing **")
        elif words_lst[0] not in cls_lst:
            print("** class doesn't exist **")
        elif len(words_lst) < 2:
            print("** instance id missing **")
        elif not flag:
            print("** no instance found **")
        elif len(words_lst) < 3 and flag:
            print("** attribute name missing **")
        elif len(words_lst) < 4 and flag:
            print("** value missing **")
        elif len(words_lst) >= 4:
            for k, v in models.storage.all().items():
                if k == key_word:
                    setattr(v, words_lst[2], words_lst[3])

    # Aliasing
    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
