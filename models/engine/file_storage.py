#!/usr/bin/python3
""" This module contains storage """
import json

class FileStorage:
    """This defines the class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Instance method"""


    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__ + obj.id] = obj.to_dict()
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        return
    def reload(self):
        """"""
        return