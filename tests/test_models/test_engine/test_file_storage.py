#!/usr/bin/python3
""" Test for FileStorage class """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """ This is a test for FileStorage class """

    def test_5_file_storage(self):
        """ Test for FileStorage Class """
        # Clean up __objects anf FileStorage attributes
        storage = FileStorage()
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
            storage.objects = {}
        storage.reload()
        # Test storage.all()
        self.assertEqual(storage.all(), {})
        base = BaseModel()
        # Build Key
        base_key = base.__class__.__name__ + '.' + base.id
        # Confirm Automatic call of storage.save() in BaseModel Instantiation
        self.assertEqual(storage.all(), {base_key: base})
        # Test storage.save() open file to confirm contents
        storage.save()
        with open(storage.file_path) as file:
            json_string = file.read()
        # Delete the file and reset __objects in FileStorage To test new()
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
            storage.objects = {}
        # Test storage.new()
        storage.new(base)
        self.assertEqual(storage.all(), {base_key: base})
        base.save()

        with open(storage.file_path) as file:
            json_string = file.read()
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
            storage.objects = {}


if __name__ == "__main__":
    unittest.main()
