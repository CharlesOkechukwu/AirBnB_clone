#!/usr/bin/python3
"""Test for User class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test for User class"""

    def test_type_of_city(self):
        """Test Instance"""
        city1 = City()
        self.assertIsInstance(city1, City)

    def test_default_attributes_of_city(self):
        """Test for default attributes"""
        city1 = City()
        self.assertEqual(city1.name, '')
        self.assertEqual(city1.state_id, '')

    def test_attributes_modification(self):
        """Test for attributes modification"""
        city1 = City()
        city1.name = "airbnb"
        city1.state_id = "1234"

        self.assertEqual(city1.name, "airbnb")
        self.assertEqual(city1.state_id, "1234")
