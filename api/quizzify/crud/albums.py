import logging

from dotenv import load_dotenv
from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor
from quizzify.utils.helpers import flatten_list
from quizzify.utils.schemas import Album

load_dotenv()
logger = logging.getLogger(__name__)


def get_albums_ids():
    """Get all the albums' IDs from the database.

    Returns
    -------
    list
        A list of all the albums' IDs.
    """
    query = sql.SQL("SELECT id FROM albums;")
    with QueryExecutor() as executor:
        albums_ids = executor.execute(query, fetch=True)
    albums_ids = [album["id"] for album in albums_ids]
    return albums_ids


def get_random_album():
    """Get a random album from the database.

    Returns
    -------
    dict
        A random album.
    """
    query = sql.SQL(
        "SELECT albums.id as album_id, albums.name as album_name, "
        "albums.popularity, albums.release_year, albums.total_tracks, "
        "albums.image_url, "
        "artists.id as artist_id, artists.name as artist_name "
        "FROM albums "
        "JOIN artists ON albums.artist_id = artists.id "
        "OFFSET floor(random() * (SELECT COUNT(*) FROM artists))"
        "LIMIT 1;"
    )
    with QueryExecutor() as executor:
        random_album = executor.execute(query, fetch=True)
    return random_album


def insert_album(
    album: Album,
    artist_id: str,
):
    """Insert an album into the database.

    Parameters
    ----------
    album : Album
        The album to insert into the database.
    artist_id : str
        The artist's ID.
    """
    query = sql.SQL(
        "INSERT INTO albums "
        "(id, name, popularity, release_year, total_tracks, image_url, artist_id) "
        "VALUES "
        "(%(album_id)s, %(album_name)s, %(popularity)s, %(album_release_year)s, "
        "%(total_tracks)s, %(album_image)s, %(artist_id)s );"
    )
    variables = {
        "album_id": album.id,
        "album_name": album.name,
        "popularity": album.popularity,
        "album_release_year": album.release_year,
        "total_tracks": album.total_tracks,
        "album_image": album.image_url,
        "artist_id": artist_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)
