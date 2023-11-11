#!/usr/bin/python3
""" Test for FileStorage class """
from models.base_model import BaseModel
from models.engine import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ This is a test for FileStorage class """
    def SetUp(self):
        """Setup Method"""
        base1 = BaseModel()
        storage = FileStorage()
        
    def TearDown(self):
        """Tear down class"""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_5_file_storage(self):
        """ Test for FileStorage Class """

        self.assertEqual(storage.all, {})
        base2 = BaseModel()
        storage.new(base2)
        key = self.__class__.__name__ + base2.id
        self.assertEqual(storage.all, {key : base2})
        storage.save()
        with open("file.json") as file:
            json_data = file.read()
        self.assertEqual(
                json_data,
                "\{{}: {}\}".format(key, base2.to_dict())
        )
        base1.save()
        key1 = self.__class__.__name__ + base1.id
        self.assertEqual(storage.all, {key: base2, key1: base1.to_dict()})
