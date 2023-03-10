import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Steve", 50, "Copperhead Road")
        self.guest2 = Guest("Stevi", 200, "Dreams")


    def test_guests_have_name(self):
        self.assertEqual("Steve", self.guest1.name)
        self.assertEqual("Stevi", self.guest2.name)

    def test_guests_have_wallet(self):
        self.assertEqual(50, self.guest1.wallet)
        self.assertEqual(200, self.guest2.wallet)

    def test_guests_have_favourite_song(self):
        self.assertEqual("Copperhead Road", self.guest1.favourite_song)
        self.assertEqual("Dreams", self.guest2.favourite_song)