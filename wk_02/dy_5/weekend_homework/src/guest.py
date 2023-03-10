class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def song_is_favourite(self, song):
        if self.favourite_song == song.name:
            return f"{self.name}'s favourite song!"

