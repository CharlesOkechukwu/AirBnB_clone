#!/usr/bin/python3
"""Test for User class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test for User class"""

    def test_type_of_amenity(self):
        """Test Instance"""
        amenity1 = Amenity()
        self.assertIsInstance(amenity1, Amenity)

    def test_default_attributes_of_amenity(self):
        """Test for default attributes"""
        amenity1 = Amenity()
        self.assertEqual(amenity1.name, '')

    def test_attributes_modification(self):
        """Test for attributes modification"""
        amenity1 = Amenity()
        amenity1.name = "airbnb"

        self.assertEqual(amenity1.name, "airbnb")
