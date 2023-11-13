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
        store = FileStorage()
        self.assertIsInstance(store, FileStorage)

    def test_type_all(self):
        """ Test for FileStorage Class """
        all = models.storage.all()
        self.assertIsInstance(all, dict)

    def test_new_method(self):
        """Test New"""
        old_dict = models.storage.all().copy()
        base = BaseModel()
        new_dict = models.storage.all().copy()
        self.assertGreater(len(new_dict), len(old_dict))

    def test_save_method(self):
        """Test save() method"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists("file.json"))

    # def test_reload_method(self):
    #     """Test reload() method"""
    #     if os.path.exists("file.json"):
    #         os.remove("file.json")
    #     models.storage.reload()
    #     self.assertEqual(models.storage.all(), {})
    #     a = models.storage.all().copy()
    #     base = BaseModel()
    #     base.save()
    #     models.storage.reload()
    #     self.assertNotEqual(a, models.storage.all())


if __name__ == "__main__":
    unittest.main()
