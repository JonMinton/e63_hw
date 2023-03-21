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

# # # * List All Artists/Albums (`select_all`)
all_artists = artist_repository.select_all()

for x in all_artists:
    print(f"{x.name} has id {x.id}")



# # * Delete all Artists / Albums

artist_repository.delete_all()
# album_repository.delete_all()

all_artists = artist_repository.select_all()

if len(all_artists) == 0:
    print("Deletion worked :)")


# # * Find Artists/Albums by their ID (`select`)

artist_repository.save(artist2)
artist_repository.save(artist3)

all_artists_now = artist_repository.select_all()

for x in all_artists_now:
    print(f"{x.name} has id {x.id}")

selected_new_artist = artist_repository.select_by_id(23)
# print(len(all_new_artists))
# print(selected_new_artist.name)



# # Every artist should have a name, and each album should have a name/title, genre and artist.

# # ## Further tasks

# # Additionally it would be nice to be able to:

# # * List all the albums by an artist
# album_repository.get_albums_by_this_artist(artist)


# # * Edit Artists/Albums
# artist_repository.edit(id, new_values)
# album_repository.edit(id. new_values)

# # * Delete Artists/Albums
# artist_repository.delete(id)
# album_repository.delete(id)


# # Remember to regularly git commit!