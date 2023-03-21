from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository


def save(album):
    sql = "INSERT INTO albums (name, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select_by_id( row['artist_id'] )
        album = Album(row['name'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums    

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_by_id(id):
    artist = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

     # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        selected_album = results[0]
        artist = artist_repository.select_by_id(selected_album['artist_id'])

        album = Album(selected_album['name'], selected_album['genre'], artist, selected_album['id'])
    return album

def get_valid_ids():
    sql = "SELECT id from albums"
    results = run_sql(sql)
    ids = []
    if results:
        for row in results:
            ids.append(row["id"])
    return ids

def get_albums_by_this_artist(artist):
    sql = "select * from albums where artist_id = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    if results:
        albums = []
        for row in results:
            this_album = Album(row["name"], row["genre"], artist, row["id"])
            albums.append(this_album)
        return albums
    
def update(album):

    sql = """
        UPDATE albums 
            SET (name, genre, artist_id, id) 
                = (%s, %s, %s, %s) 
            WHERE id = %s
    """
    values = [
        album.name, album.genre, album.artist.id, album.id,
            album.id
    ]

    run_sql(sql, values)