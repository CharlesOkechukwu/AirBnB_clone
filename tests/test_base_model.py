#!/usr/bin/python3
"""Test for BaseModel"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""

    def test_3_base_model(self):
        """Test for 3-basemodel"""
        base1 = BaseModel()
        self.assertIsInstance(base1, BaseModel)
        self.assertEqual(
            str(base1),
            "[BaseModel] (83147678-b5ff-4dce-a1ba-9d6ea93b42dd) {'id': "
            "'83147678-b5ff-4dce-a1ba-9d6ea93b42dd', 'created_at': datet"
            "ime.datetime(2023, 11, 9, 22, 32, 26, 226566), 'updated_at':"
            " datetime.datetime(2023, 11, 9, 22, 32, 26, 226650)}" 
            )
        base1.name = "Abdul"
        base1.number = 54
        base1.created_at = datetime(2023, 11, 9, 22, 32, 26, 226566)
        base1.updated_at = datetime(2023, 11, 9, 22, 32, 26, 226650)

