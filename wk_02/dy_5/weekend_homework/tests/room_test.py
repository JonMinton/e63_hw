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

        self.song1 = Song("Jeremy", 3.40)
        self.song2 = Song("Song 2", 2.01)
        self.song3 = Song("Down in a Hole", 4.15)
        self.song4 = Song("Everclear", 4.20)
        self.song5 = Song("Dark Side of the Moon", 7.23)
        self.song6 = Song("Money", 5.12)


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

    def test_room_can_play_song_in_playlist(self):
        self.room1.add_song_to_playlist(self.song1)
        self.room1.add_song_to_playlist(self.song2)
        self.assertEqual(2, len(self.room1.songs))
        self.room1.checkin_guest(self.guest1)
        self.assertEqual(0, self.room1.songs_played)
        self.room1.play_song(self.song1)
        self.assertEqual(1, self.room1.songs_played)
        self.room1.play_song(self.song3)
        self.assertEqual(1, self.room1.songs_played)
        self.room1.checkin_guest(self.guest3)
        self.room1.play_song(self.song2)
        self.assertEqual(2, self.room1.songs_played)
    
    def test_room_can_play_songs_even_if_empty(self):
        self.room1.add_song_to_playlist(self.song1)
        self.assertEqual(1, len(self.room1.songs))
        self.assertEqual(0, len(self.room1.guests))
        self.room1.play_song(self.song1)
        self.assertEqual(1, self.room1.songs_played)

    def test_room_playing_song_updates_guests_record_of_favourite_songs_heard(self):
        self.room1.add_song_to_playlist(self.song2)
        self.assertEqual(1, len(self.room1.songs))
        self.assertEqual(0, len(self.room1.guests))
        self.room1.checkin_guest(self.guest3)
        self.assertEqual(1, len(self.room1.guests))
        self.assertEqual(0, self.guest3.times_favourite_song_heard)
        self.room1.play_song(self.song2)
        self.assertEqual(1, self.guest3.times_favourite_song_heard)
        self.room1.add_song_to_playlist(self.song1)
        self.room1.play_song(self.song1)
        self.assertEqual(1, self.guest3.times_favourite_song_heard)
        self.assertEqual(2, self.room1.songs_played)

