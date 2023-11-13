#!/usr/bin/python3
"""Perform Unittest for FileStorage class
test methods and instantiation
"""
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import json


class TestFileStorage(unittest.TestCase):
    """Test filestorage methods and instantiation"""
    def test_instantiation(self):
        """test file storage instance type"""
        f1 = FileStorage()
        self.assertEqual(type(f1), FileStorage)

    def test_file_path(self):
        """test file path type to ensure it is a string"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_all(self):
        """test all method in FileStorage"""
        f1 = FileStorage()
        self.assertEqual(type(f1.all()), dict)

    def test_new(self):
        """Test the new method in FileStorage"""
        f1 = FileStorage()
        b1 = BaseModel()
        u1 = User()
        s1 = State()
        c1 = City()
        a1 = Amenity()
        p1 = Place()
        r1 = Review()
        f1.new(b1)
        f1.new(u1)
        f1.new(s1)
        f1.new(c1)
        f1.new(a1)
        f1.new(p1)
        f1.new(r1)
        self.assertIn("BaseModel" + '.' + b1.id, f1.all().keys())
        self.assertIn("User" + '.' + u1.id, f1.all().keys())
        self.assertIn("State" + '.' + s1.id, f1.all().keys())
        self.assertIn("City" + '.' + c1.id, f1.all().keys())
        self.assertIn("Amenity" + '.' + a1.id, f1.all().keys())
        self.assertIn("Place" + '.' + p1.id, f1.all().keys())
        self.assertIn("Review" + '.' + r1.id, f1.all().keys())
