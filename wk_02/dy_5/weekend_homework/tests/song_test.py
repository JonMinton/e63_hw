import unittest

from src.song import Song, ms

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Rumours", ms(4.0, 18.0))
        self.song2 = Song("Copperhead Road", ms(4.0, 29.0))

    def test_songs_have_names(self):
        self.assertEqual("Rumours", self.song1.name)
        self.assertEqual("Copperhead Road", self.song2.name)

    def test_songs_have_durations(self):
        self.assertEqual(4.00 + 18.00 / 60.00, self.song1.duration)
        self.assertEqual(4.00 + 29.00 / 60.00, self.song2.duration)