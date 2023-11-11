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
        self.assertEqual(str(storage.all()), {})
        base1 = BaseModel()
        base2 = BaseModel()
        key1 = base1.__class__.__name__ + base1.id
        key2 = base2.__class__.__name__ + base2.id
        self.assertEqual(storage.all(), {key1: base1, key2 : base2})
        base1.save()
        with open(storage.file_path, "r") as file:
            json_data = file.read()
        self.assertEqual(
                json_data,
                "\{{}: {}, {}: {}\}".format(key1, base1.to_dict(), key2, base2.to_dict())
        )
        if os.path.isfile(storage.file_path):
            os.remove(storage.file_path)
        base1.save()
        with open(storage.file_path, "r") as file:
            json_data = file.read()
        self.assertEqual(
                json_data,
                "\{{}: {}, {}: {}\}".format(key1, base1.to_dict(), key2, base2.to_dict())
        )

if __name__ == "__main__":
    unittest.main()
