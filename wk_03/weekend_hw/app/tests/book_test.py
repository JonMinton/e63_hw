import unittest

from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("The Red Book", "Mick Crimson", "Romance")
        self.book2 = Book("The Green Book", "Jane Verdanti", "Ecology")

    def test_books_have_titles(self):
        self.assertEqual("The Red Book", self.book1.title)
        self.assertEqual("The Green Book", self.book2.title)

