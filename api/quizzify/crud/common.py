from psycopg2.extras import RealDictCursor

from quizzify.db.session import connect_to_db


def get_random_artist_song():
    """Get a random artist and song from the database.

    Returns
    -------
    dict
        A random song and its artist.
    """
    connection = connect_to_db()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query=(
            "SELECT songs.name AS song_name, artists.name AS artist_name "
            "FROM songs "
            "INNER JOIN artists "
            "ON songs.artist_id = artists.id "
            "OFFSET floor(random() * (SELECT COUNT(*) FROM songs))"
            "LIMIT 1;"
        )
    )
    random_artist_song = cursor.fetchone()
    cursor.close()
    connection.close()
    return random_artist_song
