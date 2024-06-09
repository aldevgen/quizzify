from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor


def get_random_artist_song():
    """Get a random artist and song from the database.

    Returns
    -------
    dict
        A random song and its artist.
    """
    query = sql.SQL(
        "SELECT songs.name AS song_name, artists.name AS artist_name "
        "FROM songs as songs "
        "LEFT JOIN artists as artists "
        "ON songs.artist_id = artists.id "
        "OFFSET floor(random() * (SELECT COUNT(*) FROM songs)) "
        "LIMIT 1;"
    )
    with QueryExecutor() as executor:
        random_artist_song = executor.execute(query, fetch=True, one=True)
    return random_artist_song
