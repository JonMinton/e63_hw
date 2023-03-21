from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository



# You have been asked to create an app that will allow a music collector to manage their collection of CDs/records.

# In their console they would like to be able to:

# * Create and Save Artists

artist1 = Artist("Eddie Vedder")
artist2 = Artist("Thom York")
artist3 = Artist("Randy Newman")
artist4 = Artist("Guy Garvey")

# * Create and Save Albums
artist_repository.save(artist1)
album_repository.save(
    Album("Ten", "Rock", artist1)
)


# # # * List All Artists/Albums (`select_all`)
all_artists = artist_repository.select_all()

for x in all_artists:
    print(f"{x.name} has id {x.id}")

all_albums = album_repository.select_all()
# for x in all_albums:
#     print(f"{x.name} has id {x.id}")

for row in all_albums:
    print(f"ID: {row.id}, NAME: {row.name}")
print(f"there are {len(all_albums)} rows in the albums table")

# # # * Delete all Artists / Albums

# artist_repository.delete_all()
# all_remaining_albums = album_repository.delete_all()

# print(f"After deleting all, there are now {len(all_remaining_albums)} rows in the albums table")

# all_artists = artist_repository.select_all()

# if len(all_artists) == 0:
#     print("Deletion worked :)")


# # # * Find Artists/Albums by their ID (`select`)

get_album_ids = album_repository.get_valid_ids()

get_artist_ids = artist_repository.get_valid_ids()

specific_artist = artist_repository.select_by_id(str(get_artist_ids[0]))
print(f"the specific artist is {specific_artist.name}")

specific_album = album_repository.select_by_id(str(get_album_ids[0]))
print(f"the specific album is {specific_album.name}")

# # Every artist should have a name, and each album should have a name/title, genre and artist.

# # ## Further tasks

# # Additionally it would be nice to be able to:

# # * List all the albums by an artist
albums_by_artist = album_repository.get_albums_by_this_artist(artist1)
print(f"The artist {artist1.name} has the following albums:")

for row in albums_by_artist:
    print(f"{row.name}")


# # * Edit Artists/Albums
# artist_repository.edit(id, new_values)
# album_repository.edit(id. new_values)

# # * Delete Artists/Albums
# artist_repository.delete(id)
# album_repository.delete(id)


# # Remember to regularly git commit!