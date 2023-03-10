import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Steve", 50, "Copperhead Road")
        self.guest2 = Guest("Stevi", 200, "Dreams")

        self.song1 = Song("Dreams", 4.10)
        self.song2 = Song("Dadedah", 20.05)
        self.song3 = Song("Copperhead Road", 3.80)


    def test_has_name(self):
        self.assertEqual("Steve", self.guest1.name)
        self.assertEqual("Stevi", self.guest2.name)

    def test_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)
        self.assertEqual(200, self.guest2.wallet)

    def test_has_favourite_song(self):
        self.assertEqual("Copperhead Road", self.guest1.favourite_song)
        self.assertEqual("Dreams", self.guest2.favourite_song)

    def test_current_song_is_favourite(self):
        self.assertEqual(
            None, 
            self.guest1.song_is_favourite(self.song1)
        )
        self.assertEqual(
            "Stevi's favourite song!",
            self.guest2.song_is_favourite(self.song1)
        )
        self.assertEqual(
            "Steve's favourite song!",
            self.guest1.song_is_favourite(self.song3)
        )


