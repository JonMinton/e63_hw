import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song
from src.venue import Venue

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Red Room", 4)
        self.room2 = Room("Orange Room", 8)
        self.room3 = Room("Green Room", 10)
        self.room4 = Room("Yellow Room", 5)

        self.guest1 = Guest("Alice", 50, "Blah")
        self.guest2 = Guest("Bob", 100, "Science!")
        self.guest3 = Guest("Charlie", 1000, "Cottoneye Joe")
        self.guest4 = Guest("Damien", 666, "Firestarter")
        self.guest5 = Guest("Edith", 35, "We'll Meet Again")

        self.song1 = Song("Jeremy", 3.40)
        self.song2 = Song("Song 2", 2.01)
        self.song3 = Song("Down in a Hole", 4.15)
        self.song4 = Song("Everclear", 4.20)
        self.song5 = Song("Dark Side of the Moon", 7.23)
        self.song6 = Song("Money", 5.12)

        self.venue = Venue(
            "Caterwaullers", 
            20.00, 
            [self.room1, self.room2, self.room3, self.room4],
            500.00
        )


    def test_has_name(self):
        self.assertEqual("Caterwaullers", self.venue.name)

    def test_has_till(self):
        self.assertEqual(500, self.venue.till)

    def test_has_four_rooms(self):
        self.assertEqual(4, len(self.venue.rooms))

    def test_can_admit_guests(self):
        self.assertEqual(0, len(self.venue.guests))
        self.venue.admit_guest(self.guest1)
        self.assertEqual(1, len(self.venue.guests))
        self.venue.admit_guest(self.guest2)
        self.assertEqual(2, len(self.venue.guests))

    def test_guests_can_leave(self):
        self.assertEqual(0, len(self.venue.guests))
        self.venue.admit_guest(self.guest1)
        self.assertEqual(1, len(self.venue.guests))
        self.venue.remove_guest(self.guest1)
        self.assertEqual(0, len(self.venue.guests))

    def test_guests_can_enter_and_leave_rooms(self):
        self.assertEqual(0, len(self.venue.guests))
        self.assertEqual(0, len(self.room1.guests))

        self.venue.admit_guest(self.guest1)
        self.assertEqual(1, len(self.venue.guests))
        self.assertEqual(0, len(self.room1.guests))

        self.venue.transfer_guest_to_room(self.guest1, self.room1)
        self.assertEqual(0, len(self.venue.guests))
        self.assertEqual(1, len(self.room1.guests))

        self.venue.transfer_guest_from_room(self.guest1, self.room1)
        self.assertEqual(1, len(self.venue.guests))
        self.assertEqual(0, len(self.room1.guests))

    def test_guests_get_charged_fee_to_enter_venue(self):
        self.assertEqual(50.00, self.guest1.wallet)
        self.assertEqual(500.00, self.venue.till)
        self.venue.admit_guest(self.guest1)
        self.assertEqual(30.00, self.guest1.wallet)
        self.assertEqual(520.00, self.venue.till)

    def test_poor_people_cannot_enter_venue(self):
        poor_guest = Guest("Poor Paul", 15.00, favourite_song = "If I Were A Rich Man")

        self.assertEqual(15.00, poor_guest.wallet)
        self.assertEqual(500.00, self.venue.till)
        self.venue.admit_guest(poor_guest)
        self.assertEqual(15.00, poor_guest.wallet)
        self.assertEqual(500.00, self.venue.till)
        self.assertEqual(0, len(self.venue.guests))

    def test_guests_cannot_enter_room_if_above_capacity(self):
        self.assertEqual(0, len(self.venue.guests))
        self.venue.admit_guest(self.guest1)
        self.assertEqual(1, len(self.venue.guests))
        self.assertEqual(0, len(self.room1.guests))
        self.venue.transfer_guest_to_room(self.guest1, self.room1)
        self.assertEqual(0, len(self.venue.guests))
        self.assertEqual(1, len(self.room1.guests))

        self.venue.admit_guest(self.guest2)
        self.venue.admit_guest(self.guest3)
        self.venue.admit_guest(self.guest4)
        self.venue.admit_guest(self.guest5)
        self.assertEqual(4, len(self.venue.guests))
        self.assertEqual(1, len(self.room1.guests))
        self.venue.transfer_guest_to_room(self.guest2, self.room1)
        self.venue.transfer_guest_to_room(self.guest3, self.room1)
        self.venue.transfer_guest_to_room(self.guest4, self.room1)
        self.assertEqual(1, len(self.venue.guests))
        self.assertEqual(4, len(self.room1.guests))




