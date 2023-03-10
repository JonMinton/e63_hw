import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Blues Room", 10)
        self.room2 = Room("Reds Room", 2)

        self.guest1 = Guest("Steve", 50, "Copperhead Road")
        self.guest2 = Guest("Stevi", 200, "Dreams")
        self.guest3 = Guest("Damen", 30, "Song 2")


    def test_rooms_have_names(self):
        self.assertEqual("Blues Room", self.room1.name)
        self.assertEqual("Reds Room", self.room2.name)

    def test_rooms_have_capacities(self):
        self.assertEqual(10, self.room1.capacity)
        self.assertEqual(2, self.room2.capacity)

    def test_can_add_guest(self):
        self.assertEqual(0, len(self.room1.guests))
        self.room1.checkin_guest(self.guest3)
        self.assertEqual(1, len(self.room1.guests))

    def test_can_remove_guests(self):
        self.room1.checkin_guest(self.guest1)
        self.room1.checkin_guest(self.guest2)
        self.room1.checkin_guest(self.guest3)
        self.assertEqual(3, len(self.room1.guests))
        self.room1.checkout_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guests))

    def test_rooms_wont_admit_if_above_capacity(self):
        self.room2.checkin_guest(self.guest1)
        self.room2.checkin_guest(self.guest2)
        self.assertEqual(2, len(self.room2.guests))
        self.room2.checkin_guest(self.guest3)
        self.assertEqual(2, len(self.room2.guests))
