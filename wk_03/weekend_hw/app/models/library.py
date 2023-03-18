from bs4 import BeautifulSoup
import requests
import pandas as pd
import os.path
import pickle

from models.book import Book

class Library():
    def __init__(self, name, file_loc = "models/dta/secret_library.data"):
        self.name = name
        self.file_loc = file_loc
        self.library = None
        self.table_scraped = False

    def make_secret_library():
        url = "https://cultistsimulator.fandom.com/wiki/List_of_books"
        # Ask hosting server to fetch url
        pages = requests.get(url)
        # pages.text
        soup = BeautifulSoup(pages.text, 'lxml')
        # soup
        cultist_simulator_table = soup.find('table', class_='wikitable sortable')
        # cultist_simulator_table.find_all('th')

        headers = []
        for i in cultist_simulator_table.find_all('th'):
            heading_name = i.text.strip('\n')
            headers.append(heading_name)

        # headers

        mydata = pd.DataFrame(columns = headers)

        for j in cultist_simulator_table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            length = len(mydata)
            mydata.loc[length] = row

        # mydata
        secret_library = []

        n_secret_books = len(mydata)

        for i in range(n_secret_books):
            this_title = mydata["Title"][i].replace('\n', ' ').strip()
            this_language = "English" if mydata["Language"][i] == "\n" else mydata["Language"][i].replace("\n", "").strip()
            this_book = Book(this_title, "Cultist Simulator", "Occult")
            secret_library.append(this_book)

        # secret_library

        with open('models/dta/secret_library.data', 'wb') as filehandle:
            # Store the data as a binary data stream
            pickle.dump(secret_library, filehandle)

        self.library = secret_library
        self.data_scraped = True

    def get_library(self):
        if os.path.isfile(self.file_loc):
            with open(self.file_loc, 'rb') as filehandle:
            # Read the data as a binary data stream
                self.library = pickle.load(filehandle)
        else: 
            self.library = make_secret_library()

