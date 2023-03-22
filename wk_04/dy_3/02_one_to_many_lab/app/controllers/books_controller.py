from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all() # NEW
    return render_template("/books/index.html", books = books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("/books/new.html", authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route("/books",  methods=['POST'])
def create_book():
    print(request.form)
    title           = request.form['title']
    author_id       = request.form['author_id']
    genre           = request.form['genre']
    year_published  = request.form['year_published']
    author          = author_repository.select(author_id)
    book            = Book(title, genre, year_published, author)
    book_repository.save(book)
    return redirect('/books')


# SHOW
# GET '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('/books/show.html', book = book)

# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template('/books/edit.html', book = book, authors = authors)

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title           = request.form['title']
    author_id       = request.form['author_id']
    genre           = request.form['genre']
    year_published  = request.form['year_published']
    author          = author_repository.select(author_id)
    book            = Book(title, genre, year_published, author, id)
    book_repository.save(book)
    return redirect('/books')

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['GET'])
def delete_book(id):
    print(f"id to delete: {id}")
    book_repository.delete(id)
    return redirect('/books')
