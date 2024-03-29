from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, year_published, author_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.year_published, book.author.id]
    for v in values:
        print(v)
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], row['year_published'], author, row['id'] )
        books.append(book)
    return books



def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)


    if results:
        result = results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['year_published'], author, result['id'] )
        return book
    else:
        return None


def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(book):
    sql = "UPDATE books SET (title, genre, year_published, author_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.year_published, book.author.id, book.id]
    run_sql(sql, values)

def books_by_author(author):
    books = []

    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['genre'], row['year_published'], author, row['id'])
        books.append(book)
    return books
