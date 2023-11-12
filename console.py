#!/usr/bin/python3
"""This module has a class"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class represents the console"""
    prompt = "(hbnb) "

    def precmd(self, line):
        """Executes before line"""
        pattern = re.compile(r"(\S+)\.(\S+)\((.*)\)")
        match = pattern.search(line)
        if not match:
            return line

        matched = match.groups()
        if matched[1] == "all":
            return "{} {}".format(matched[1], matched[0])
        elif matched[1] == "count":
            count = 0
            for i in storage.all().keys():
                pattern = re.compile(r"{}".format(matched[0]))
                if pattern.match(i):
                    count += 1
            print(count)
            return "\n"
        elif matched[1] in ["show", "destroy"]:
            return "{} {} {}".format(matched[1], matched[0], matched[2][1:-1])
        elif matched[1] == "update":
            args = matched[2].split(", ")
            if args[1][0] == "{":
                obj_key = "{}.{}".format(matched[0], eval(matched[2])[0])
                if obj_key in storage.all():
                    obj = storage.all()[obj_key]
                    update_dict = eval(matched[2])[1]
                    for key, value in update_dict.items():
                        setattr(obj, key, value)
                    storage.save()
                else:
                    print("** no instance found **")
                return "\n"
            elif len(args) == 3:
                return "{} {} {} {} {}".format(
                        matched[1], matched[0],
                        args[0][1:-1], args[1][1:-1], args[2])
        else:
            return "command doesn't exist"

    def do_EOF(self, line):
        """Quits the program"""
        print()
        return True

    def do_quit(self, line):
        """Quits the program"""
        return True

    def emptyline(self):
        """Shouldn't execute anything"""
        pass

    def check_class(self, class_name):
        """Check if the class exists."""
        if class_name not in [
                "BaseModel", "User", "Place",
                "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, line):
        """Creates a new instance of a class, saves it, and prints the id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif not self.check_class(args[0]):
            return
        else:
            instance = globals()[args[0]]()
            storage.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif not self.check_class(args[0]):
            return
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif not self.check_class(args[0]):
            return
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                del storage.all()[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of instances."""
        args = line.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif not self.check_class(args[0]):
            return
        else:
            for obj_key in storage.all().keys():
                class_name = obj_key.split(".")[0]
                if class_name == args[0]:
                    obj_list.append(str(storage.all()[obj_key]))
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = []
        in_quotes = False
        current_arg = ""

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
            print("** class name missing **")
        elif not self.check_class(args[0]):
            return
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                instance = storage.all()[obj_key]
                attribute_name = args[2]
                value = args[3]
                setattr(instance, attribute_name, value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
