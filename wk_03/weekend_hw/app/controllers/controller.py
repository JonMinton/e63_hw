from flask import render_template, request, redirect
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os.path
import pickle

from models.book import Book
from models.library import Library
from app import app

lib_obj = Library("My library")
lib_obj.get_library()
all_books = lib_obj.library

# all_books[13].checked_out = True

@app.route('/books')
def index():
    return render_template('index.html', title="Jon's Occult Library", books = all_books)

@app.route('/')
def root_index():
    return redirect('/books')

@app.route('/books/<index>')
def read(index):
    return render_template('specific_book.html', this_book = all_books[int(index)], this_index = int(index))


@app.route('/books', methods=['POST'])
def add_book():
  bookTitle = request.form['title']
  newBook = Book(title=bookTitle, author = "", genre = "", checked_out = False)
  all_books.append(newBook)

  return redirect('/books')

@app.route('/books', methods=['DELETE'])
def delete_book():
    book_title = request.form['book_name']
    # book_to_destroy = [book for book in books if book.title == name]
    print(f"The book's title is {book_title}")
    # for book in all_books:
    #     if book.title == bookTitle:
    #         print("Found book!")
    #         all_books.remove(book)

    return redirect('/books')