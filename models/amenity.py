#!/usr/bin/python3
""" This module contains the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This defines the Amenity class"""
    name = ''

    def __str__(self):
        """ A nicely printable string representation of the
            object Amenity
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[Amenity] ({:s}) {}".format(self.id, dict_display)
