from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists    

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_by_id(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        artist = Artist(result['name'], result['id'] )
    return artist

def get_valid_ids():
    sql = "SELECT id from artists"
    results = run_sql(sql)
    ids = []
    if results:
        for row in results:
            ids.append(row["id"])
    return ids

def update(artist):

    sql = """
        UPDATE artists 
            SET (name, id) 
                = (%s, %s) 
            WHERE id = %s
    """
    values = [
        artist.name, artist.id,
            artist.id
    ]

    run_sql(sql, values)

