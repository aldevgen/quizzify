-- This file is used to create the tables in the database when the server starts up.
-- The tables are only created if they do not already exist in the database.

----------------------------------------------------------------------------------------
-------------------------------- Relation Spotify Users --------------------------------
----------------------------------------------------------------------------------------

--    column_name    |     data_type
---------------------+-------------------
-- spotify_id        | character varying
-- spotify_username  | character varying
-- spotify_email     | character varying
-- spotify_image_url | character varying
-- spotify_uri       | character varying

DROP TABLE IF EXISTS users_spotify CASCADE;

CREATE TABLE users_spotify (
  spotify_id VARCHAR(50) PRIMARY KEY,
  spotify_username VARCHAR(100),
  spotify_email VARCHAR(150),
  spotify_image_url VARCHAR(100),
  spotify_uri VARCHAR(100)
);

----------------------------------------------------------------------------------------
------------------------------------ Relation Users ------------------------------------
----------------------------------------------------------------------------------------

-- column_name |          data_type
---------------+-----------------------------
-- user_id     | character varying
-- username    | character varying
-- email       | character varying
-- hashed_pwd  | bytea
-- created_at  | timestamp without time zone

DROP TABLE IF EXISTS users_quizzify CASCADE;

CREATE TABLE users_quizzify (
  user_id VARCHAR(50) PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  hashed_pwd BYTEA,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users_spotify (spotify_id)
);

----------------------------------------------------------------------------------------
----------------------------------- Relation Artists -----------------------------------
----------------------------------------------------------------------------------------

-- column_name |     data_type
---------------+-------------------
-- id          | character varying
-- name        | character varying
-- popularity  | integer
-- genres      | character varying []
-- followers   | integer
-- image_url   | character varying

DROP TABLE IF EXISTS artists CASCADE;

CREATE TABLE artists (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(100),
  popularity INT,
  genres VARCHAR(50) [],
  followers INT,
  image_url VARCHAR(150)
);

----------------------------------------------------------------------------------------
------------------------------- Relation Related Artists -------------------------------
----------------------------------------------------------------------------------------

-- column_name        |     data_type
----------------------+-------------------
-- artist_id          | character varying
-- related_artist_id  | character varying


DROP TABLE IF EXISTS related_artists CASCADE;

CREATE TABLE related_artists (
  artist_id VARCHAR(50),
  related_artist_id VARCHAR(50),
  FOREIGN KEY (artist_id) REFERENCES artists (id),
  FOREIGN KEY (related_artist_id) REFERENCES artists (id)
);

----------------------------------------------------------------------------------------
--------------------------------- Relation Top Artists ---------------------------------
----------------------------------------------------------------------------------------

-- column_name |     data_type
---------------+-------------------
-- artist_id   | character varying
-- name        | character varying
-- popularity  | integer
-- image_url   | character varying

DROP TABLE IF EXISTS top_artists CASCADE;

CREATE TABLE top_artists (
  artist_id VARCHAR(50),
  user_id VARCHAR(50),
  FOREIGN KEY (artist_id) REFERENCES artists (id),
  FOREIGN KEY (user_id) REFERENCES users_quizzify (user_id)
);

----------------------------------------------------------------------------------------
----------------------------------- Relation Albums ------------------------------------
----------------------------------------------------------------------------------------

-- column_name    |     data_type
------------------+-------------------
-- id             | character varying
-- name           | character varying
-- popularity     | integer
-- release_year   | date
-- release_decade | date
-- total_tracks   | integer
-- image_url      | character varying
-- artist_id      | character varying, foreign key

DROP TABLE IF EXISTS albums CASCADE;

CREATE TABLE albums (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(200),
  popularity INT,
  release_year VARCHAR(4),
  release_decade VARCHAR(4),
  total_tracks INT,
  image_url VARCHAR(150),
  artist_id VARCHAR(25),
  FOREIGN KEY (artist_id) REFERENCES artists (id)
);

----------------------------------------------------------------------------------------
------------------------------ Relation Artist's Albums --------------------------------
----------------------------------------------------------------------------------------

-- column_name |     data_type
---------------+-------------------
-- artist_id   | character varying
-- album_id    | character varying

DROP TABLE IF EXISTS albums_artists CASCADE;

CREATE TABLE albums_artists (
  artist_id VARCHAR(50),
  album_id VARCHAR(50),
  FOREIGN KEY (artist_id) REFERENCES artists (id),
  FOREIGN KEY (album_id) REFERENCES albums (id)
);

----------------------------------------------------------------------------------------
--------------------------------- Relation Top Albums ----------------------------------
----------------------------------------------------------------------------------------

-- column_name  |     data_type
----------------+-------------------
-- album_id     | character varying
-- user_id      | character varying

DROP TABLE IF EXISTS top_albums CASCADE;

CREATE TABLE top_albums (
  album_id VARCHAR(50),
  user_id VARCHAR(50),
  FOREIGN KEY (album_id) REFERENCES albums (id),
  FOREIGN KEY (user_id) REFERENCES users_quizzify (user_id)
);


----------------------------------------------------------------------------------------
------------------------------------ Relation Songs ------------------------------------
----------------------------------------------------------------------------------------

-- column_name  |     data_type
----------------+-------------------
-- id           | character varying
-- name         | character varying
-- popularity   | integer
-- duration_ms  | integer
-- track_number | integer
-- artist_id    | character varying, foreign key
-- album_id     | character varying, foreign key

DROP TABLE IF EXISTS songs;

CREATE TABLE songs (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(200),
  popularity INT,
  duration_ms INT,
  track_number INT,
  artist_id VARCHAR(25),
  album_id VARCHAR(25),
  FOREIGN KEY (artist_id) REFERENCES artists (id),
  FOREIGN KEY (album_id) REFERENCES albums (id)
);

----------------------------------------------------------------------------------------
---------------------------------- Relation Top Songs ----------------------------------
----------------------------------------------------------------------------------------

-- column_name  |     data_type
----------------+-------------------
-- song_id      | character varying
-- user_id      | character varying, foreign key

DROP TABLE IF EXISTS top_songs;

CREATE TABLE top_songs (
  song_id VARCHAR(50),
  user_id VARCHAR(50),
  FOREIGN KEY (song_id) REFERENCES songs (id),
  FOREIGN KEY (user_id) REFERENCES users_quizzify (user_id)
);
