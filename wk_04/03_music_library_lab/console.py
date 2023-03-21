from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository



# You have been asked to create an app that will allow a music collector to manage their collection of CDs/records.

album_repository.delete_all()
artist_repository.delete_all()

# In their console they would like to be able to:

# * Create and Save Artists

artist1 = Artist("Eddie Vedder")
artist2 = Artist("Thom York")


# * Create and Save Albums
print("creating album1 and artist1")
artist_repository.save(artist1)
album_repository.save(
    Album("Ten", "Rock", artist1)
)

print("creating album2 and artist2")
artist_repository.save(artist2)
album_repository.save(
    Album("Kid A", "Electronica", artist2)
)

print("Showing artists after creations")
# # # * List All Artists/Albums (`select_all`)
all_artists = artist_repository.select_all()
for x in all_artists:
    print(f"{x.name} has id {x.id}")

print("Showing albums after creation")
all_albums = album_repository.select_all()
for x in all_albums:
    print(f"{x.name} has id {x.id}")


# * Delete all Artists / Albums

print("Deleting artists and then albums")
artist_repository.delete_all()
album_repository.delete_all()

print("Confirming that after deleting all artists the table has nothing to show")
all_artists = artist_repository.select_all()
if len(all_artists) == 0:
    print("the artists table is now empty: Success!")
else: 
    print("The artists table is not empty: Failure!")

print("Confirming that after deleting all albums the table has nothing to show")
all_albums = album_repository.select_all()
if len(all_albums) == 0:
    print("the albums table is now empty: Success!")
else: 
    print("The albums table is not empty: Failure!")


print("Checking can access albums and artists by their id")

print("First creating two new artists")

artist3 = Artist("Randy Newman")
artist4 = Artist("Guy Garvey")

print("... and adding them")
artist_repository.save(artist3)
artist_repository.save(artist4)

print("Confirming both have been added")
all_artists = artist_repository.select_all()

for row in all_artists:
    print(f"ID: {row.id}, NAME: {row.name}")


print("Now the same with two albums")

album_repository.save(
    Album("12 Songs", "Singer-Songwriter", artist3)
)

album_repository.save(
    Album("Asleep In The Back", "Rock", artist4)
)

print("Confirming they've been added too")
all_albums = album_repository.select_all()

for row in all_albums:
    print(f"ID: {row.id}, NAME: {row.name}, GENRE: {row.genre}, ARTIST: {row.artist.name}")

print("""
    As the IDs are unique and keep changing, I've added a function
    which returns the valid IDs. I'll use this to individually get 
    the first then the second entry in both tables (As there are 
    currently just two records in each table)
""")

artist_table_valid_ids = artist_repository.get_valid_ids()
album_table_valid_ids = album_repository.get_valid_ids()

first_individual_artist = artist_repository.select_by_id(
    artist_table_valid_ids[0]
)

second_individual_artist = artist_repository.select_by_id(
    artist_table_valid_ids[1]
)


first_individual_album = album_repository.select_by_id(
    album_table_valid_ids[0]
)

second_individual_album = album_repository.select_by_id(
    album_table_valid_ids[1]
)

print(f"First artist: ID: {first_individual_artist.id}, NAME: {first_individual_artist.name}")
print(f"Second artist: ID: {second_individual_artist.id}, NAME: {second_individual_artist.name}")
print(f"First album: ID: {first_individual_album.id}, NAME: {first_individual_album.name}")
print(f"Second album: ID: {second_individual_artist.id}, NAME: {second_individual_artist.name}")


print("List albums by artist")

print("For this I'll add a second album by Randy Newman")

album_repository.save(
    Album("Land of Dreams", "Soft Rock", artist3)
)

albums_by_newman = album_repository.get_albums_by_this_artist(artist3)
albums_by_garvey = album_repository.get_albums_by_this_artist(artist4)

print(f"There are {len(albums_by_newman)} albums by {artist3.name}")
for x in albums_by_newman:
    print(f"- {x.name}")
print(f"There are {len(albums_by_garvey)} albums by {artist4.name}")
for x in albums_by_garvey:
    print(f"- {x.name}")


print("Editing an artist")

print("Before the edit:")
for x in all_artists:
    print(f"{x.name} has id {x.id}")

print("After the edit:")
artist3.name = "Randy Oldman"
artist_repository.update(artist3)

all_artists = artist_repository.select_all()
for x in all_artists:
    print(f"{x.name} has id {x.id}")

print("""
n.b. I've had two Randy Newman concerts cancelled due to slow 
recovery from knee operations, so think the name change is valid!
"""
)

print("Finally, deleting an individual artist")

artist_repository.delete(artist_table_valid_ids[1])

all_artists = artist_repository.select_all()
print("Artists after deletion")
for x in all_artists:
    print(f"- {x.name} has id {x.id}")

all_albums = album_repository.select_all()
print("Albums after deletion")
for x in all_albums:
    print(f"- {x.name} has id {x.id}")

print("So, deleting the artist has also deleted their albums")

print("Let's now confirm that an individual album can be deleted directly")

album_ids = album_repository.get_valid_ids()
album_repository.delete(album_ids[0])

print("After direct deletion:")

print("Albums after deletion")
all_albums = album_repository.select_all()
for x in all_albums:
    print(f"- {x.name} has id {x.id}")

# # # ## Further tasks

# # # Additionally it would be nice to be able to:

# # # * List all the albums by an artist
# albums_by_artist = album_repository.get_albums_by_this_artist(artist1)
# print(f"The artist {artist1.name} has the following albums:")

# for row in albums_by_artist:
#     print(f"{row.name}")


# # # * Edit Artists/Albums
# artist1.name = "Beddie Bedder"
# artist_repository.update(artist1)

# all_artists = artist_repository.select_all()

# for row in all_artists:
#     print(f"NAME: {row.name} has ID: {row.id}")


# # artist_repository.edit(id, new_values)
# # album_repository.edit(id. new_values)

# # # * Delete Artists/Albums
# # artist_repository.delete(id)
# # album_repository.delete(id)


# # # Remember to regularly git commit!