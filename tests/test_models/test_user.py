#!/usr/bin/python3
"""
unittest for the Place module
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    unittest for the place class
    """
    def test_instances_type(self):
        user_1 = User()
        self.assertIs(type(user_1), User)
        self.assertIsInstance(user_1.id, str)
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.last_name, str)
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
        self.assertIsInstance(user_1.updated_at, datetime)
        self.assertIsInstance(user_1.created_at, datetime)
    
    def test_rev_str_repr(self):
        user_2 = User()
        str_format = "[User] ({}) {}".format(user_2.id, user_2.__dict__)
        self.assertEqual(user_2.__str__(), str_format)

    def _users_ids(self):
        user_1 = User()
        user_2 = User()
        self.assertNotEqual(user_1.id, user_2.id)

    def test_place_save(self):
        user_1 = User()
        updated_before_save = user_1.updated_at
        user_1.save()
        updated_after_save = user_1.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)

    def test_place_to_dict(self):
        user_one = User()

        user_one.first_name = "fatima"
        user_one.last_name = "hafsa"
        user_one.email = "fatima.hafsa@we.com"
        user_one.password = "notyourbusiness"

        self.assertIn("id", user_one.to_dict())
        self.assertIn("first_name", user_one.to_dict())
        self.assertIn("last_name", user_one.to_dict())
        self.assertIn("email", user_one.to_dict())
        self.assertIn("password", user_one.to_dict())
        self.assertIn("created_at", user_one.to_dict())
        self.assertIn("updated_at", user_one.to_dict())
        self.assertIn("__class__", user_one.to_dict())
