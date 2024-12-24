import logging

from dotenv import load_dotenv
from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor
from quizzify.utils.schemas import Song

load_dotenv()
logger = logging.getLogger(__name__)


def get_songs_ids():
    """Get all the songs' IDs from the database.

    Returns
    -------
    list
        A list of all the songs' IDs.
    """
    query = sql.SQL("SELECT id FROM songs;")
    with QueryExecutor() as executor:
        songs_ids = executor.execute(query, fetch=True)
    songs_ids = [song_id["id"] for song_id in songs_ids]
    return songs_ids


def get_random_song(user_id: str):
    """Get a random song from the database.

    Returns
    -------
    dict
        A random song.
    """
    query = sql.SQL(
        "SELECT "
        "songs.id as song_id, "
        "songs.name as song_name, "
        "artists.id as artist_id, "
        "artists.name as artist_name, "
        "albums.id as album_id, "
        "albums.name as album_name, "
        "songs.popularity, "
        "songs.duration_ms, "
        "songs.track_number "
        "FROM top_songs "
        "LEFT JOIN songs "
        "ON top_songs.song_id = songs.id "
        "LEFT JOIN artists "
        "ON songs.artist_id = artists.id "
        "LEFT JOIN albums ON songs.album_id = albums.id "
        "WHERE user_id = %(user_id)s "
        "ORDER BY RANDOM() "
        "LIMIT 1;"
    )
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        random_song = executor.execute(
            query,
            variables=variables,
            fetch=True,
            one=True,
        )
    return random_song


def insert_song(
    song: Song,
):
    """Insert a song into the database.

    Parameters
    ----------
    song : Song
        The song to insert into the database.
    """
    query = sql.SQL(
        "INSERT INTO songs "
        "(id, name, artist_id, album_id, popularity, duration_ms, track_number) "
        "VALUES"
        "(%(song_id)s, %(song_name)s, %(artist_id)s, %(album_id)s, %(popularity)s, "
        "%(duration_ms)s, %(track_number)s);"
    )
    variables = {
        "song_id": song.id,
        "song_name": song.name,
        "artist_id": song.artist_id,
        "album_id": song.album_id,
        "popularity": song.popularity,
        "duration_ms": song.duration_ms,
        "track_number": song.track_number,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables=variables)


def get_top_songs(
    user_id: str,
    limit: int = 10,
):
    """Get the user's top songs.

    Parameters
    ----------
    user_id : str
        The user's ID.
    limit : int, optional
        The number of songs to return, by default 10.

    Returns
    -------
    list
        The user's top songs.
    """
    query = sql.SQL(
        "SELECT "
        "songs.id as song_id, "
        "songs.name as song_name, "
        "artists.id as artist_id, "
        "artists.name as artist_name, "
        "albums.id as album_id, "
        "albums.name as album_name, "
        "songs.popularity "
        "FROM top_songs "
        "LEFT JOIN songs "
        "ON top_songs.song_id = songs.id "
        "LEFT JOIN artists "
        "ON songs.artist_id = artists.id "
        "LEFT JOIN albums ON songs.album_id = albums.id "
        "WHERE user_id = %(user_id)s"
        "LIMIT  %(limit)s ;"
    )
    variables = {
        "limit": limit,
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        top_songs = executor.execute(query, variables=variables, fetch=True)
    return top_songs


def get_top_songs_ids(user_id: str):
    """Get the top songs' IDs for a user.

    This method is only used for testing purposes.

    Parameters
    ----------
    user_id : str
        The user's ID.

    Returns
    -------
    list
        The top songs' IDs for the given user.
    """
    query = sql.SQL("SELECT song_id FROM top_songs WHERE user_id = %(user_id)s;")
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        top_songs_ids = executor.execute(query, variables=variables, fetch=True)
    top_songs_ids = [song_id["song_id"] for song_id in top_songs_ids]
    return top_songs_ids


def insert_top_song_user(
    song_id: str,
    user_id: str,
):
    """Insert user as having listened to a song.

    Parameters
    ----------
    song_id : str
        The song's ID.
    user_id : str
        The user's ID.
    """
    query = sql.SQL(
        "INSERT INTO top_songs "
        "(song_id, user_id) "
        "VALUES "
        "(%(song_id)s, %(user_id)s);"
    )
    variables = {
        "song_id": song_id,
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)
