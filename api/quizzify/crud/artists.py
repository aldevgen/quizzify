import logging
from typing import Dict, List

from dotenv import load_dotenv
from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor
from quizzify.utils.schemas import Artist

load_dotenv()
logger = logging.getLogger(__name__)


def get_artists_ids() -> List[str]:
    """Get all the artists' IDs from the database.

    Returns
    -------
    list
        A list of all the artists' IDs.
    """
    query = sql.SQL("SELECT id FROM artists;")
    with QueryExecutor() as executor:
        artists_ids = executor.execute(query, fetch=True)
    artists_ids = [artist["id"] for artist in artists_ids]
    return artists_ids


def get_random_artist(user_id: str) -> Dict:
    """Get a random album from the database.

    Parameters
    ----------
    user_id : str
        The user's ID.

    Returns
    -------
    dict
        A random album.
    """
    query = sql.SQL(
        "SELECT "
        "albums.id as album_id, "
        "albums.name as album_name, "
        "artists.id as artist_id, "
        "artists.name as artist_name, "
        "artists.popularity, "
        "artists.genres, "
        "artists.image_url "
        "FROM top_artists "
        "LEFT JOIN albums_artists "
        "ON albums_artists.artist_id = top_artists.artist_id "
        "LEFT JOIN artists "
        "ON artists.id = top_artists.artist_id "
        "LEFT JOIN albums "
        "ON albums_artists.artist_id = artists.id "
        "WHERE top_artists.user_id = %(user_id)s "
        "ORDER BY RANDOM() "
        "LIMIT 1;"
    )
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        random_artist = executor.execute(
            query, variables=variables, fetch=True, one=True
        )
    return random_artist


def get_artist_name(artist_id: str) -> str:
    """Get the artist's name from its ID.

    Parameters
    ----------
    artist_id : str
        The artist's ID.

    Returns
    -------
    str
        The artist's name.
    """
    query = sql.SQL("SELECT name FROM artists WHERE id = %(artist_id)s;")
    variables = {
        "artist_id": artist_id,
    }
    with QueryExecutor() as executor:
        artist_name = executor.execute(
            query,
            variables=variables,
            fetch=True,
            one=True,
        )
    return artist_name["name"]


def get_random_related_artist(
    artist_id: str,
    nb_artists: int = 3,
):
    """Get a random album from the database.

    Returns
    -------
    dict
        A random album.
    """
    query = sql.SQL(
        "SELECT related_artist_id "
        "FROM related_artists "
        "WHERE artist_id = %(artist_id)s "
        "ORDER BY RANDOM() "
        "LIMIT %(nb_artists)s;"
    )
    variables = {
        "artist_id": artist_id,
        "nb_artists": nb_artists,
    }
    with QueryExecutor() as executor:
        random_artists = executor.execute(
            query,
            variables=variables,
            fetch=True,
        )
    return random_artists


def get_random_related_artist_ids(
    artist_id: str,
    nb_artists: int = 3,
) -> List:
    """Get a random album from the database.

    Returns
    -------
    dict
        A random album.
    """
    query = sql.SQL(
        "SELECT related_artist_id "
        "FROM related_artists "
        "WHERE artist_id = %(artist_id)s "
        "ORDER BY RANDOM() "
        "LIMIT %(nb_artists)s;"
    )
    variables = {
        "artist_id": artist_id,
        "nb_artists": nb_artists,
    }
    with QueryExecutor() as executor:
        random_artist = executor.execute(
            query,
            variables=variables,
            fetch=True,
        )
    random_artist_ids = [artist["related_artist_id"] for artist in random_artist]
    return random_artist_ids


def insert_artist(
    artist: Artist,
):
    """Insert an artist into the database.

    Parameters
    ----------
    artist : Artist
        The artist to insert into the database.
    """
    query = sql.SQL(
        "INSERT INTO artists "
        "(id, name, popularity, genres, followers, image_url) "
        "VALUES "
        "(%(artist_id)s, %(artist_name)s, %(popularity)s, %(genres)s, "
        "%(followers)s, %(artist_image)s);"
    )
    variables = {
        "artist_id": artist.id,
        "artist_name": artist.name,
        "popularity": artist.popularity,
        "genres": artist.genres,
        "followers": artist.followers,
        "artist_image": artist.image_url,
    }
    with QueryExecutor() as executor:
        executor.execute(query=query, variables=variables)


def insert_top_artist_user(
    artist_id: str,
    user_id: str,
):
    """Insert user as having listened to an artist.

    Parameters
    ----------
    artist_id : str
        The artist's ID.
    user_id : str
        The user's ID.
    """
    query = sql.SQL(
        "INSERT INTO top_artists "
        "(artist_id, user_id) "
        "VALUES "
        "(%(artist_id)s, %(user_id)s);"
    )
    variables = {
        "artist_id": artist_id,
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)


def insert_related_artist_user(
    artist_id: str,
    related_artist_id: str,
):
    """Insert an artist as related to a listened artist.

    Parameters
    ----------
    artist_id : str
        The artist's ID.
    related_artist_id : str
        The related artist's ID.
    """
    query = sql.SQL(
        "INSERT INTO related_artists "
        "(artist_id, related_artist_id) "
        "VALUES "
        "(%(artist_id)s, %(related_artist_id)s);"
    )
    variables = {
        "artist_id": artist_id,
        "related_artist_id": related_artist_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)
