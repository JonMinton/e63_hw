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
    return render_template(
        'index.html', 
        title="Jon's Occult Library", 
        books = all_books,
        n_checked_out = sum([x.checked_out for x in all_books])
    )

@app.route('/')
def root_index():
    return redirect('/books')

@app.route('/books/<index>')
def read(index):
    return render_template(
        'specific_book.html', 
        this_book = all_books[int(index)], 
        this_index = int(index), 
        n_books = len(all_books)
    )


@app.route('/books', methods=['POST'])
def add_book():
  bookTitle = request.form['title']
  author    = request.form['author']
  genre     = request.form['genre']
  newBook = Book(title=bookTitle, author = author, genre = genre, checked_out = False)
  all_books.append(newBook)

  return redirect('/books')

@app.route('/books/delete', methods=['POST'])
def delete_book():
    book_to_destroy = [book for book in all_books if book.title == request.form["book_name"]]
    all_books.remove(book_to_destroy[0])
 
    return redirect('/books')

@app.route('/books/check_in', methods=['POST'])
def check_in_book():
    book_index = int(request.form["check_in"])
    book_to_check_in = all_books[book_index]
    book_to_check_in.checked_out = False

    return redirect('/books')

@app.route('/books/check_out', methods=['POST'])
def check_out_book():
    book_index = int(request.form["check_out"])
    book_to_check_out = all_books[book_index]
    book_to_check_out.checked_out = True

    return redirect('/books')
