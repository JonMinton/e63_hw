class Song:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

def ms(min, seconds):
    return min + seconds / 60.0