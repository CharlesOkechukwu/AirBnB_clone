#!/usr/bin/python3
""" This module contains storage """
import json
from models.base_model import BaseModel


class FileStorage:
    """This defines the class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(obj).split()[0].strip("[]") + '.' + obj.id
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
                self.__objects[key] = (BaseModel(**value))
        except FileNotFoundError:
            return
