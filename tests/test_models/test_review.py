#!/usr/bin/python3
"""Test for User class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test for User class"""

    def test_type_of_review(self):
        """Test Instance"""
        review1 = Review()
        self.assertIsInstance(review1, Review)

    def test_default_attributes_of_review(self):
        """Test for default attributes"""
        review1 = Review()
        self.assertEqual(review1.place_id, '')
        self.assertEqual(review1.user_id, '')
        self.assertEqual(review1.text, '')

    def test_attributes_modification(self):
        """Test for attributes modification"""
        review1 = Review()
        review1.place_id = "airbnb@email.com"
        review1.user_id = "1234"
        review1.text = "Alx"

        self.assertEqual(review1.place_id, "airbnb@email.com")
        self.assertEqual(review1.user_id, "1234")
        self.assertEqual(review1.text, "Alx")
