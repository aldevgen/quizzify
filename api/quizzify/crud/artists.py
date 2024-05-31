import logging

from dotenv import load_dotenv
from psycopg2 import sql
from psycopg2.extras import RealDictCursor

from quizzify.db.query_executor import QueryExecutor
from quizzify.db.session import connect_to_db
from quizzify.utils.schemas import Artist

load_dotenv()
logger = logging.getLogger(__name__)


def get_artists_ids():
    """Get all the artists' IDs from the database.

    Returns
    -------
    list
        A list of all the artists' IDs.
    """
    query = sql.SQL("SELECT id FROM artists;")
    with QueryExecutor() as executor:
        artists_ids = executor.execute(query, fetch=True)
    return artists_ids


def get_random_artist():
    """Get a random artist from the database.

    Returns
    -------
    dict
        A random artist.
    """
    connection = connect_to_db()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query=(
            "SELECT id, name, popularity, image_url FROM artists OFFSET floor("
            "random() * (SELECT COUNT(*) FROM artists)) LIMIT 1;"
        )
    )
    random_artist = cursor.fetchone()
    cursor.close()
    connection.close()
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
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        query=(
            "INSERT INTO artists "
            "(id, name, popularity, genres, followers, image_url, user_id) "
            "VALUES"
            "(%(artist_id)s, %(artist_name)s, %(popularity)s, %(genres)s, "
            "%(followers)s, %(artist_image)s, %(user_id)s);"
        ),
        vars={
            "artist_id": artist.id,
            "artist_name": artist.name,
            "popularity": artist.popularity,
            "genres": artist.genres,
            "followers": artist.followers,
            "artist_image": artist.image_url,
            "user_id": user_id,
        },
    )
    connection.commit()
    cursor.close()
    connection.close()
