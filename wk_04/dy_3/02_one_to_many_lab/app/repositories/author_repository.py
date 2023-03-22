from db.run_sql import run_sql

from models.author import Author



def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id



def select_all():
    authors = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    if results:
        for row in results:
            author = Author(row['first_name'], row['last_name'], row['id'] )
            users.append(author)

        return users


def select(id):
    author = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        author = Author(result['first_name'], result['last_name'], result['id'] )
    else:
        return None
    
    return Author


def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(author):
    sql = "UPDATE authors SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [author.first_name, author.last_name, author.id]
    run_sql(sql, values)
