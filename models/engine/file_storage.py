#!/usr/bin/python3
""" This module contains storage """
import json
from models.base_model import BaseModel
from models.user import User
import os


class FileStorage:
    """This defines the class FileStorage"""
    __file_path = os.getcwd() + "/file.json"
    __objects = {}

    @property
    def file_path(self):
        """Returns the file path"""
        return self.__file_path

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        json_string = json.dumps(temp)
        # validate length

        with open(self.__file_path, "w") as file:
            file.write(json_string)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists otherwise it does nothing."""
        try:
            with open(self.__file_path, "r") as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                if value["__class__"] == "BaseModel":
                    self.__objects[key] = (BaseModel(**value))
                if value["__class__"] == "User":
                    self.__objects[key] = (User(**value))
        except FileNotFoundError:
            return
