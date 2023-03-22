class Book:
    def __init__(self, title, genre, year_published, author, id = None):
        self.title = title
        self.genre = genre
        self.year_published = year_published
        self.author = author
        self.id = id