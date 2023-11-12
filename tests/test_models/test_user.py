#!/usr/bin/python3
"""Test for User class"""
import re
import unittest
from models.base_model import BaseModel
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Test for User class"""

    def test_type_of_user(self):
        """Test Instance"""
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_default_attributes_of_user(self):
        """Test for default attributes"""
        user1 = User()
        self.assertEqual(user1.email, '')
        self.assertEqual(user1.password, '')
        self.assertEqual(user1.first_name, '')
        self.assertEqual(user1.last_name, '')

    def test_attributes_modification(self):
        """Test for attributes modification"""
        user1 = User()
        user1.email = "airbnb@email.com"
        user1.password = "1234"
        user1.first_name = "Alx"
        user1.last_name = "Africa"

        self.assertEqual(user1.email, "airbnb@email.com")
        self.assertEqual(user1.password, "1234")
        self.assertEqual(user1.first_name, "Alx")
        self.assertEqual(user1.last_name, "Africa")
