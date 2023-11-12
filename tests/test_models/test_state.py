#!/usr/bin/python3
"""Test for User class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test for User class"""

    def test_type_of_state(self):
        """Test Instance"""
        state1 = State()
        self.assertIsInstance(state1, State)

    def test_default_attributes_of_state(self):
        """Test for default attributes"""
        state1 = State()
        self.assertEqual(state1.name, '')

    def test_attributes_modification(self):
        """Test for attributes modification"""
        state1 = State()
        state1.name = "airbnb"

        self.assertEqual(state1.name, "airbnb")
