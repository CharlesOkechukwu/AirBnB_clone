#!/usr/bin/python3
"""
This module contains BaseModel that defines all common
attributes/methods for other classes.
"""
import re
from datetime import datetime
import models
from uuid import uuid4


class BaseModel():
    """
    defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """ Instance method"""
        if kwargs or len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    the_date = [int(i) for i in re.split("[-:.T]", str(value))]
                    self.__dict__[key] = datetime(
                        year=the_date[0],
                        month=the_date[1],
                        day=the_date[2],
                        hour=the_date[3],
                        second=the_date[4],
                        microsecond=the_date[5]
                    )
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        for key, value in models.storage.all().items():
            if self.id == value.id:
                return
        models.storage.new(self)

    def __str__(self):
        """ A nicely printable string representation of the
            object BaseModel
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[BaseModel] ({:s}) {}".format(self.id, dict_display)

    def save(self):
        """updates the public instance attribute updated_at with
            the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        self.__dict__["__class__"] = str(self).split()[0].strip("[]")
        dict_copy = dict(self.__dict__)
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
