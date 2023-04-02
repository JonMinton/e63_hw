from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

authors_blueprint = Blueprint("authors", __name__)

@authors_blueprint.route("/authors")
def authors():
    authors = author_repository.select_all() # NEW
    return render_template("/authors/index.html", authors = authors)

@authors_blueprint.route("/authors/<id>")
def books_by_author(id):
    author = author_repository.select(id)
    print(f"author name {author.first_name} {author.last_name}")
    books = book_repository.books_by_author(author)
    return render_template("/authors/books_by_author", author = author, books = books)
