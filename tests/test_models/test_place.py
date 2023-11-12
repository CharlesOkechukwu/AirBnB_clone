#!/usr/bin/python3
"""Test for User class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test for User class"""

    def test_type_of_place(self):
        """Test Instance"""
        place1 = Place()
        self.assertIsInstance(place1, Place)

    def test_default_attributes_of_place(self):
        """Test for default attributes"""
        place1 = Place()
        self.assertEqual(place1.city_id, '')
        self.assertEqual(place1.user_id, '')
        self.assertEqual(place1.name, '')
        self.assertEqual(place1.description, '')
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1.amenity_ids, '')

    def test_attributes_modification(self):
        """Test for attributes modification"""
        place1 = Place()

        place1.city_id = 'Lagos'
        place1.user_id = 'Student'
        place1.name = 'Airbnb'
        place1.description = 'Big room'
        place1.number_rooms = 2
        place1.number_bathrooms = 2
        place1.max_guest = 2
        place1.price_by_night = 2
        place1.latitude = 15.43
        place1.longitude = 73.43
        place1.amenity_ids = 'Amenity'

        self.assertEqual(place1.city_id, 'Lagos')
        self.assertEqual(place1.user_id, 'Student')
        self.assertEqual(place1.name, 'Airbnb')
        self.assertEqual(place1.description, 'Big room')
        self.assertEqual(place1.number_rooms, 2)
        self.assertEqual(place1.number_bathrooms, 2)
        self.assertEqual(place1.max_guest, 2)
        self.assertEqual(place1.price_by_night, 2)
        self.assertEqual(place1.latitude, 15.43)
        self.assertEqual(place1.longitude, 73.43)
        self.assertEqual(place1.amenity_ids, 'Amenity')
