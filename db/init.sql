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

DROP TABLE IF EXISTS spotify_users CASCADE;

CREATE TABLE spotify_users (
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

DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
  user_id VARCHAR(50) PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(150) UNIQUE NOT NULL,
  hashed_pwd BYTEA,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES spotify_users (spotify_id)
);

----------------------------------------------------------------------------------------
--------------------------------- Relation Top Artists ---------------------------------
----------------------------------------------------------------------------------------

-- column_name |     data_type
---------------+-------------------
-- id          | character varying
-- name        | character varying
-- popularity  | integer
-- image_url   | character varying

DROP TABLE IF EXISTS top_artists CASCADE;

CREATE TABLE top_artists (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(100),
  popularity INT,
  genres VARCHAR(50) [],
  followers INT,
  image_url VARCHAR(150),
  user_id VARCHAR(50),
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);

----------------------------------------------------------------------------------------
--------------------------------- Relation Top Albums ----------------------------------
----------------------------------------------------------------------------------------

-- column_name  |     data_type
----------------+-------------------
-- id           | character varying
-- name         | character varying
-- artist_id    | character varying, foreign key
-- popularity   | integer
-- release_year | date
-- total_tracks | integer

DROP TABLE IF EXISTS top_albums CASCADE;

CREATE TABLE top_albums (
  id VARCHAR(50) PRIMARY KEY,
  name VARCHAR(200),
  popularity INT,
  release_year VARCHAR(4),
  total_tracks INT,
  image_url VARCHAR(150),
  artist_id VARCHAR(25),
  user_id VARCHAR(50),
  FOREIGN KEY (artist_id) REFERENCES top_artists (id),
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);

----------------------------------------------------------------------------------------
---------------------------------- Relation Top Songs ----------------------------------
----------------------------------------------------------------------------------------

-- column_name  |     data_type
----------------+-------------------
-- id           | character varying
-- name         | character varying
-- artist_id    | character varying, foreign key
-- album_id     | character varying, foreign key
-- popularity   | integer
-- duration_ms  | integer
-- track_number | integer

DROP TABLE IF EXISTS top_songs;

CREATE TABLE top_songs (
  id VARCHAR(50),
  name VARCHAR(200),
  popularity INT,
  duration_ms INT,
  track_number INT,
  artist_id VARCHAR(25),
  album_id VARCHAR(25),
  user_id VARCHAR(50),
  PRIMARY KEY (id, artist_id, album_id),
  FOREIGN KEY (artist_id) REFERENCES top_artists (id),
  FOREIGN KEY (album_id) REFERENCES top_albums (id),
  FOREIGN KEY (user_id) REFERENCES users (user_id)
);
