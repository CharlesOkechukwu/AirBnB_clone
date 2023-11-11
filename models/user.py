#!/usr/bin/python3
""" This module contains the User class """
from models.base_model import BaseModel


class User(BaseModel):
    """This defines the user class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __str__(self):
        """ A nicely printable string representation of the
            object User
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[User] ({:s}) {}".format(self.id, dict_display)
