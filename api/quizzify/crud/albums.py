import logging

from dotenv import load_dotenv
from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor
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


def get_random_album(user_id: str):
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
        "albums.popularity, "
        "albums.release_year, "
        "albums.release_decade, "
        "albums.total_tracks, "
        "albums.image_url, "
        "artists.id as artist_id, "
        "artists.name as artist_name "
        "FROM top_albums "
        "LEFT JOIN albums "
        "ON albums.id = top_albums.album_id "
        "LEFT JOIN artists "
        "ON artists.id = albums.artist_id "
        "WHERE top_albums.user_id = %(user_id)s "
        "ORDER BY RANDOM() "
        "LIMIT 1;"
    )
    variables = {
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        random_album = executor.execute(
            query,
            variables=variables,
            fetch=True,
            one=True,
        )
    return random_album


def get_artists_albums_ids(artist_id: str):
    """Get all the albums from the database by artist ID.

    Parameters
    ----------
    artist_id : str
        The artist's ID.

    Returns
    -------
    list
        A list of all the artist's albums.
    """
    query = sql.SQL(
        "SELECT "
        "albums.id as album_id "
        "FROM albums "
        "LEFT JOIN artists "
        "ON artists.id = albums.artist_id "
        "WHERE artist_id = %(artist_id)s;"
    )
    variables = {
        "artist_id": artist_id,
    }
    with QueryExecutor() as executor:
        raw_albums = executor.execute(query, variables=variables, fetch=True)
        albums = [album["album_id"] for album in raw_albums]
    return albums


def get_artists_albums(artist_id: str):
    """Get all the albums from the database by artist ID.

    Parameters
    ----------
    artist_id : str
        The artist's ID.

    Returns
    -------
    list
        A list of all the artist's albums.
    """
    query = sql.SQL(
        "SELECT "
        "albums.id as album_id, "
        "albums.name as album_name, "
        "artists.id as artist_id, "
        "artists.name as artist_name "
        "FROM albums "
        "LEFT JOIN artists "
        "ON artists.id = albums.artist_id "
        "WHERE artist_id = %(artist_id)s;"
    )
    variables = {
        "artist_id": artist_id,
    }
    with QueryExecutor() as executor:
        albums = executor.execute(query, variables=variables, fetch=True)
    return albums


def get_random_album_name_by_artist_id_exclude_album(
    artist_id: str,
    exclude_album_id: str,
    limit: int = 3,
) -> list:
    """Get a random album from the database by artist ID.

    This method fetches random albums from the database by artist ID by excluding the
    current album.

    Parameters
    ----------
    artist_id : str
        The artist's ID.
    exclude_album_id : str
        The album's ID to exclude.
    limit : int, optional
        The number of albums to return, by default 3.

    Returns
    -------
    list
        A list containing the names of the random albums.
    """
    query = sql.SQL(
        "SELECT albums.name as album_name "
        "FROM artists "
        "JOIN albums "
        "ON albums.artist_id = artists.id "
        "WHERE artists.id = %(artist_id)s "
        "AND albums.id != %(album_id)s "
        "ORDER BY RANDOM() "
        "LIMIT %(limit)s;"
    )
    variables = {
        "artist_id": artist_id,
        "album_id": exclude_album_id,
        "limit": limit,
    }
    with QueryExecutor() as executor:
        raw_random_albums = executor.execute(
            query,
            variables=variables,
            fetch=True,
        )
        random_albums = [album["album_name"] for album in raw_random_albums]
    return random_albums


def get_random_album_name_by_artist_id(
    artist_id: str,
    limit: int = 1,
):
    """Get one or multiple random albums from the database by artist ID.

    Parameters
    ----------
    artist_id : str
        The artist's ID.
    limit : int, optional
        The number of albums to return, by default 1.
    """
    query = sql.SQL(
        "SELECT albums.name as album_name "
        "FROM artists "
        "JOIN albums "
        "ON albums.artist_id = artists.id "
        "WHERE artists.id = %(artist_id)s "
        "ORDER BY RANDOM() "
        "LIMIT %(limit)s;"
    )
    variables = {
        "artist_id": artist_id,
        "limit": limit,
    }
    with QueryExecutor() as executor:
        if limit == 1:
            raw_random_album = executor.execute(
                query,
                variables=variables,
                fetch=True,
                one=True,
            )
            return raw_random_album["album_name"]
        else:
            raw_random_albums = executor.execute(
                query,
                variables=variables,
                fetch=True,
            )
            random_albums = [album["album_name"] for album in raw_random_albums]
            return random_albums


def insert_album(
    album: Album,
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
        "("
        "id, name, popularity, release_year, release_decade, total_tracks, image_url "
        ") "
        "VALUES "
        "("
        "%(album_id)s, %(album_name)s, %(popularity)s, %(album_release_year)s, "
        "%(album_release_decade)s, %(total_tracks)s, %(album_image)s "
        ");"
    )
    variables = {
        "album_id": album.id,
        "album_name": album.name,
        "popularity": album.popularity,
        "album_release_year": album.release_year,
        "album_release_decade": album.release_decade,
        "total_tracks": album.total_tracks,
        "album_image": album.image_url,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)


def insert_album_artist(
    album_id: str,
    artist_id: str,
):
    """Insert an album's artist into the database.

    Parameters
    ----------
    album_id : str
        The album's ID.
    artist_id : str
        The artist's ID.
    """
    query = sql.SQL(
        "INSERT INTO albums_artists "
        "(album_id, artist_id) "
        "VALUES "
        "(%(album_id)s, %(artist_id)s);"
    )
    variables = {
        "album_id": album_id,
        "artist_id": artist_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)


def insert_top_album_user(
    album_id: str,
    user_id: str,
):
    """Insert user as having listened to an album.

    Parameters
    ----------
    album_id : str
        The album's ID.
    user_id : str
        The user's ID.
    """
    query = sql.SQL(
        "INSERT INTO top_albums "
        "(album_id, user_id) "
        "VALUES "
        "(%(album_id)s, %(user_id)s);"
    )
    variables = {
        "album_id": album_id,
        "user_id": user_id,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables)
