#!/usr/bin/python3
""" This module contains the Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """This defines the Place class"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ''

    def __str__(self):
        """ A nicely printable string representation of the
            object Place
        """
        dict_display = self.__dict__.copy()
        if "__class__" in dict_display.keys():
            dict_display.pop("__class__")
        return "[Place] ({:s}) {}".format(self.id, dict_display)
