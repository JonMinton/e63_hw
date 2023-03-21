from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist


def save(user):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user
