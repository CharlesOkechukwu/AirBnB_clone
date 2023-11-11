#!/usr/bin/python3
""" This module contains the Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """This defines the Review class"""
    place_id = ''
    user_id = ''
    text = ''

    def __str__(self):
        """ A nicely printable string representation of the
            object Review
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[Review] ({:s}) {}".format(self.id, dict_display)
