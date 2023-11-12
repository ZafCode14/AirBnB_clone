#!/usr/bin/env python3
"""

    Class BaseModel defines all common attributes/methods for other classes

"""
import uuid
import datetime
import models


class BaseModel:
    """ Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = self.created_at
        s_fmt = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "created_at":
                        setattr(self, k, self.created_at.strptime(v, s_fmt))
                    elif k == "updated_at":
                        setattr(self, k, self.updated_at.strptime(v, s_fmt))
                    else:
                        setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """ Return str [<class name>] (<self.id>) <self.__dict__> """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self) -> None:
        """ Updates attribute updated_at with the current datetime """
        self.updated_at = datetime.datetime.today()
        models.storage.save()

    def to_dict(self) -> dict:
        """ Returns a dictionary containing all keys/values """
        obj_dct = self.__dict__.copy()
        obj_dct["__class__"] = self.__class__.__name__
        obj_dct["created_at"] = self.created_at.isoformat()
        obj_dct["updated_at"] = self.updated_at.isoformat()
        return obj_dct
