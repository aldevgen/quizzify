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
    query = sql.SQL("SELECT id FROM top_artists;")
    with QueryExecutor() as executor:
        artists_ids = executor.execute(query, fetch=True)
    artists_ids = [artist["id"] for artist in artists_ids]
    return artists_ids


def get_random_artist() -> Dict:
    """Get a random artist from the database.

    Returns
    -------
    dict
        A random artist.
    """
    query = sql.SQL(
        "SELECT id, name, popularity, image_url FROM top_artists "
        "OFFSET floor(random() * (SELECT COUNT(*) FROM top_artists)) "
        "LIMIT 1;"
    )
    with QueryExecutor() as executor:
        random_artist = executor.execute(query, fetch=True)
    return random_artist


def insert_artist(
    artist: Artist,
    user_id: str,
):
    """Insert an artist into the database.

    Parameters
    ----------
    artist : Artist
        The artist to insert into the database.
    user_id : str
        The user's ID.
    """
    query = sql.SQL(
        "INSERT INTO top_artists "
        "(id, name, popularity, genres, followers, image_url, user_id) "
        "VALUES "
        "(%(artist_id)s, %(artist_name)s, %(popularity)s, %(genres)s, "
        "%(followers)s, %(artist_image)s, %(user_id)s);"
    )
    variables = {
        "artist_id": artist.id,
        "artist_name": artist.name,
        "popularity": artist.popularity,
        "genres": artist.genres,
        "followers": artist.followers,
        "artist_image": artist.image_url,
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query=query, variables=variables)
