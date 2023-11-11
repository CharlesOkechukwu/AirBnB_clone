#!/usr/bin/python3
""" This module contains the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """This defines the City class"""
    state_id = ''
    name = ''

    def __str__(self):
        """ A nicely printable string representation of the
            object City
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[City] ({:s}) {}".format(self.id, dict_display)
