import unittest
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os.path
import pickle

from models.book import Book
from models.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.fake_loc = "path/to/nowhere"
        self.my_lib = Library("My first occult library")

    def test_library_object_exists(self):
        self.assertEqual("My first occult library", self.my_lib.name)

    def test_library_is_initially_none(self):
        self.assertEqual(None, self.my_lib.library)

    def test_library_is_not_none_after_method_run(self):
        self.my_lib.get_library()
        self.assertEqual(236, len(self.my_lib.library))

    def test_library_does_not_scrape_as_data_available_locally(self):
        self.assertEqual(False, self.my_lib.table_scraped)
        self.my_lib.get_library()
        self.assertEqual(False, self.my_lib.table_scraped)

    def test_books_in_library_are_books_and_readable(self):
        self.my_lib.get_library()
        self.assertEqual("A Catalogue of Uncharted Pleasures", self.my_lib.library[0].title)
        self.assertEqual("A True and Complete Accounting of the Asclepian Mysteries of the Roots of the House", self.my_lib.library[6].title)
        self.assertEqual("Five Creations", self.my_lib.library[135].title)


