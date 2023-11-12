#!/usr/bin/python3
""" Test for FileStorage class """
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """ This is a test for FileStorage class """

    def test_instance(self):
        """Test Instance"""
        store = models.engine.file_storage.FileStorage()
        self.assertIsInstance(store, models.engine.file_storage.FileStorage)

    def test_type_all(self):
        """ Test for FileStorage Class """
        all = models.storage.all()
        self.assertIsInstance(all, dict)

    def test_new_(self):
        """Test New"""
        
        base = BaseModel()
        base_key = base.__class__.__name__ + '.' + base.id
        base.save()
        storage.save()
        storage.new(base)
        self.assertEqual(storage.all(), {base_key: base})
        with open(storage.file_path) as file:
            json_string = file.read()
        if os.path.exists(storage.file_path):
            os.remove(storage.file_path)
        
        self.assertEqual(storage.all(), {base_key: base})
        base.save()


if __name__ == "__main__":
    unittest.main()
