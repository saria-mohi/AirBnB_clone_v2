#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.__init__ import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from console import HBNBCommand

class Test_PlaceModel(unittest.TestCase):
    """
    Test the place model class
    """

    def setUp(self):
        self.cli = HBNBCommand()
        self.model = Place()
        self.model.save()

    def tearDown(self):
        self.cli.do_destroy("Place " + self.model.id)

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "city_id"))
        self.assertTrue(hasattr(self.model, "user_id"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "description"))
        self.assertTrue(hasattr(self.model, "number_rooms"))
        self.assertTrue(hasattr(self.model, "number_bathrooms"))
        self.assertTrue(hasattr(self.model, "max_guest"))
        self.assertTrue(hasattr(self.model, "price_by_night"))
        self.assertTrue(hasattr(self.model, "latitude"))
        self.assertTrue(hasattr(self.model, "longitude"))
        self.assertTrue(hasattr(self.model, "amenities"))
        self.assertEqual(self.model.city_id, "")
        self.assertEqual(self.model.user_id, "")
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.description, "")
        self.assertEqual(self.model.number_rooms, 0)
        self.assertEqual(self.model.number_bathrooms, 0)
        self.assertEqual(self.model.max_guest, 0)
        self.assertEqual(self.model.price_by_night, 0)
        self.assertEqual(self.model.latitude, 0.0)
        self.assertEqual(self.model.longitude, 0.0)
        self.assertEqual(self.model.amenities, [''])


if __name__ == "__main__":
    unittest.main()
