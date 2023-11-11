#!/usr/bin/python3
"""Test for BaseModel"""
import re
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test for BaseModel"""

    def test_3_base_model(self):
        """Test for 3-basemodel"""
        base1 = BaseModel()
        base2 = BaseModel()

        self.assertIsInstance(base1, BaseModel)
        self.assertNotEqual(base1.id, base2.id)

        self.assertEqual(
            base1.id,
            str(
                re.search(
                    "^[a-z0-9]{8,8}-[a-z0-9]{4,4}-"
                    "[a-z0-9]{4,4}-[a-z0-9]{4,4}-"
                    "[a-z0-9]{12,12}$",
                    base1.id
                    ).group()
                )
            )
        self.assertIsInstance(base1.created_at, datetime.datetime)
        self.assertEqual(
            str(base1.created_at),
            str(
                re.search(
                    "^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:"
                    "[0-9]{2,2}:[0-9]{2,2}.[0-9]{6,6}$",
                    str(base1.created_at)
                    ).group()
                )
            )
        self.assertIsInstance(base1.updated_at, datetime.datetime)
        self.assertEqual(
            str(base1.updated_at),
            str(
                re.search(
                    "^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:"
                    "[0-9]{2,2}:[0-9]{2,2}.[0-9]{6,6}$",
                    str(base1.updated_at)
                    ).group()
                )
            )
        self.assertEqual(
            str(base1),
            "[BaseModel] ({}) {}".format(base1.id, base1.__dict__)
        )
        base1.name = "Abdul"
        self.assertEqual(base1.name, "Abdul")
        base1.number = 54
        self.assertEqual(base1.number, 54)
        previous_updated_at = base1.updated_at
        base1.save()
        self.assertTrue(previous_updated_at < base1.updated_at)
        dict_base = base1.to_dict()
        self.assertIsInstance(dict_base, dict)
        self.assertEqual(dict_base["name"], "Abdul")
        self.assertEqual(dict_base["number"], 54)
        self.assertEqual(dict_base["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
