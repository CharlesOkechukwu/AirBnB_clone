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

        storage = FileStorage()
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
            storage.objects = {}
        storage.reload()
        self.assertEqual(storage.all(), {})
        base = BaseModel()
        base_key = base.__class__.__name__ + '.' + base.id
        self.assertEqual(storage.all(), {})
        base.save()
        with open(storage.file_path) as file:
            json_string = file.read()
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
            storage.objects = {}
        storage.new(base)
        self.assertEqual(storage.all(), {base_key: base})
        base.save()


if __name__ == "__main__":
    unittest.main()
