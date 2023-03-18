from flask import render_template, redirect
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


@app.route('/books')
def index():
    return render_template('index.html', title="Jon's Occult Library", books = all_books)

@app.route('/')
def root_index():
    return redirect('/books')


# @app.route('/orders/<index>')
# def single_order(index):
#   chosen_order = orders[int(index)]
  
#   return render_template('order.html', order=chosen_order)
