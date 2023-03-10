class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []

    def checkin_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
    
    def checkout_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_playlist(self, song):
        self.songs.append(song)

    def remove_song_from_playlist(self, song):
        self.songs.remove(song)