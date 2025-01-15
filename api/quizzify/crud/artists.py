import logging
from typing import Dict, List

from dotenv import load_dotenv
from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor
from quizzify.utils.schemas import Artist, TimeRange

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


def get_top_artists(
    user_id: str,
    limit: int = 10,
) -> List[Dict]:
    """Get the user's top artists from the database.

    Parameters
    ----------
    user_id : str
        The user's Spotify ID.
    limit : int
        The number of artists to return.

    Returns
    -------
    list
        A list of the user's top artists.
    """
    query = sql.SQL(
        "SELECT "
        "artists.id, "
        "artists.name, "
        "artists.popularity, "
        "artists.genres, "
        "artists.image_url "
        "FROM top_artists "
        "LEFT JOIN artists "
        "ON artists.id = top_artists.artist_id "
        "WHERE top_artists.user_id = %(user_id)s "
        "LIMIT %(limit)s;"
    )
    variables = {
        "user_id": user_id,
        "limit": limit,
    }
    with QueryExecutor() as executor:
        top_artists = executor.execute(
            query,
            variables=variables,
            fetch=True,
        )
    return top_artists


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
        "artists.id, "
        "artists.name, "
        "artists.popularity, "
        "artists.genres, "
        "artists.image_url "
        "FROM top_artists "
        "LEFT JOIN albums_artists "
        "ON albums_artists.artist_id = top_artists.artist_id "
        "LEFT JOIN artists "
        "ON artists.id = top_artists.artist_id "
        "WHERE top_artists.user_id = %(user_id)s "
        "ORDER BY RANDOM() "
        "LIMIT 1;"
    )
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        random_artist = executor.execute(
            query,
            variables=variables,
            fetch=True,
            one=True,
        )
    return random_artist


def get_random_artist_album(user_id: str) -> Dict:
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
        "artists.id as artist_id, "
        "artists.name as artist_name, "
        "artists.popularity, "
        "artists.genres, "
        "artists.image_url, "
        "albums.id as album_id, "
        "albums.name as album_name "
        "FROM top_artists "
        "LEFT JOIN albums_artists "
        "ON albums_artists.artist_id = top_artists.artist_id "
        "LEFT JOIN artists "
        "ON artists.id = top_artists.artist_id "
        "LEFT JOIN albums "
        "ON albums.id = albums_artists.album_id "
        "WHERE top_artists.user_id = %(user_id)s "
        "ORDER BY RANDOM() "
        "LIMIT 1;"
    )
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        random_artist = executor.execute(
            query,
            variables=variables,
            fetch=True,
            one=True,
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


def get_random_related_artists(
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
    """Get a list of random artists IDs related to a given artist.

    Returns
    -------
    list
        A list of random artists IDs related to a give artist.
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


def get_random_related_artists_name(
    artist_id: str,
    nb_artists: int = 3,
) -> List:
    """Fetch a list of random artists names related to a given artist.

    Returns
    -------
    list
        A list of random artists names related to a give artist.
    """
    query = sql.SQL(
        "SELECT "
        "artists.name as artist_name "
        "from related_artists "
        "JOIN artists "
        "ON artists.id = related_artists.related_artist_id "
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
    random_artist_ids = [artist["artist_name"] for artist in random_artist]
    return random_artist_ids


def get_top_artists_ids(user_id: str) -> List[str]:
    """Get the top artists' IDs for a given user.

    This method is only used for test purposes

    Parameters
    ----------
    user_id : str
        The user's ID.

    Returns
    -------
    list
        The top artists' IDs for the given user.
    """
    query = sql.SQL("SELECT artist_id FROM top_artists WHERE user_id = %(user_id)s;")
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        top_artists_ids = executor.execute(
            query,
            variables=variables,
            fetch=True,
        )
    top_artists_ids = [artist["artist_id"] for artist in top_artists_ids]
    return top_artists_ids


def get_related_artists_ids(artist_id: str) -> List[str]:
    """Get the related artists' IDs for a given artist.

    This method is only used for test purposes

    Parameters
    ----------
    artist_id : str
        The artist's ID.

    Returns
    -------
    list
        The related artists' IDs for the given artist.
    """
    query = sql.SQL(
        "SELECT related_artist_id "
        "FROM related_artists "
        "WHERE artist_id = %(artist_id)s;"
    )
    variables = {
        "artist_id": artist_id,
    }
    with QueryExecutor() as executor:
        related_artists_ids = executor.execute(
            query,
            variables=variables,
            fetch=True,
        )
    related_artists_ids = [
        artist["related_artist_id"] for artist in related_artists_ids
    ]
    return related_artists_ids


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
    time_range: TimeRange,
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
        "(artist_id, user_id, time_range, time_date) "
        "VALUES "
        "(%(artist_id)s, %(user_id)s, %(time_range)s, CURRENT_DATE);"
    )
    variables = {
        "artist_id": artist_id,
        "user_id": user_id,
        "time_range": time_range,
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
