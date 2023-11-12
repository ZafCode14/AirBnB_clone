#!/usr/bin/env python3
"""

    class FileStorage serializes/deserializes

"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ Instances Serializes/deserializes from/to JSON file """
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj) -> None:
        """ Sets in __objects the obj with key <obj class name>.id """
        cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self) -> None:
        """ Serializes __objects to the JSON file (path: __file_path """
        objects_with_dict = ({k: v.to_dict()
                              for k, v in FileStorage.__objects.items()})
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(objects_with_dict))

    def reload(self) -> None:
        """ Deserializes the JSON file to __objects """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                objs_dic = json.loads(f.read())
            for obj_dic in objs_dic.values():
                cls_name = obj_dic["__class__"]
                self.new(eval(cls_name)(**obj_dic))
