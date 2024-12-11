--Stephon Kumar

-- Create a table for artists
CREATE TABLE artists (
    id INTEGER PRIMARY KEY,  -- Unique ID for each artist
    name TEXT NOT NULL  -- Name of the artist
);

-- Create a table for albums
CREATE TABLE albums (
    id INTEGER PRIMARY KEY,  -- Unique ID for each album
    name TEXT NOT NULL,  -- Name of the album
    artist_id INTEGER NOT NULL,  -- Foreign key linking to the artist
    FOREIGN KEY (artist_id) REFERENCES artists (id)  -- Define relationship
);

-- Create a table for songs
CREATE TABLE songs (
    id INTEGER PRIMARY KEY,  -- Unique ID for each song
    name TEXT NOT NULL,  -- Name of the song
    album_id INTEGER NOT NULL,  -- Foreign key linking to the album
    track_number INTEGER NOT NULL,  -- The track number on the album
    duration INTEGER NOT NULL,  -- Duration of the song in seconds
    FOREIGN KEY (album_id) REFERENCES albums (id)  -- Define relationship
);
