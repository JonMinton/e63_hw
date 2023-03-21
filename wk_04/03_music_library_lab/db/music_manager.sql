DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;



CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  genre VARCHAR(255),
  artist_id INT NOT NULL REFERENCES artists(id) ON DELETE CASCADE
);


-- Do once 
-- createdb music_manager

-- also remember
-- psql -d music_manager -f db/music_manager.sql