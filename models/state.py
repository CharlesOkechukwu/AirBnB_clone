#!/usr/bin/python3
""" This module contains the State class """
from models.base_model import BaseModel


class State(BaseModel):
    """"This defines the State class"""
    name = ''

    def __str__(self):
        """ A nicely printable string representation of the
            object State
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[State] ({:s}) {}".format(self.id, dict_display)
