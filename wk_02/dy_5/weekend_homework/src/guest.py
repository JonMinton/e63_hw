class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        self.times_favourite_song_heard = 0

    def song_is_favourite(self, song):
        if self.favourite_song == song.name:
            self.times_favourite_song_heard += 1
            return f"{self.name}'s favourite song!"

