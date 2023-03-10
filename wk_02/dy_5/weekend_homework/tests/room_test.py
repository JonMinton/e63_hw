import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Blues Room", 10)
        self.room2 = Room("Reds Room", 2)

    def test_rooms_have_names(self):
        self.assertEqual("Blues Room", self.room1.name)
        self.assertEqual("Reds Room", self.room2.name)

    def test_rooms_have_capacities(self):
        self.assertEqual(10, self.room1.capacity)
        self.assertEqual(2, self.room2.capacity)