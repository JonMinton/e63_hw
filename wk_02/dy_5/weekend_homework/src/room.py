class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.songs_played = 0

    def checkin_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
    
    def checkout_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def add_song_to_playlist(self, song):
        self.songs.append(song)

    def remove_song_from_playlist(self, song):
        self.songs.remove(song)

    def play_song(self, song):
        if song.name in [x.name for x in self.songs]:
            self.songs_played += 1
            if len(self.guests) > 0:
                for guest in self.guests:
                    guest.song_is_favourite(song)