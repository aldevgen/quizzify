from dotenv import load_dotenv

from quizzify.crud import albums as crud_albums
from quizzify.crud import artists as crud
from quizzify.spotify.spotify_requests import (
    spotify_get_album,
    spotify_get_artist_albums_ids,
    spotify_get_related_artists,
    spotify_get_user_id,
    spotify_get_user_top_artists,
)
from quizzify.utils.schemas import Album, Artist, TimeRange

# load environment variables
load_dotenv()


def get_top_artists(user_id: str):
    """Get the user's top artists from the database.

    Parameters
    ----------
    user_id : str
        The user's Spotify ID.

    Returns
    -------
    list
        A list of the user's top artists.
    """
    return crud.get_top_artists(user_id=user_id)


def insert_top_artists(
    time_range: TimeRange,
    limit: int,
):
    """Get the user's top artists from Spotify.

    Parameters
    ----------
    time_range : str
        The time range for the top artists (short_term, medium_term, long_term).
            - long_term (calculated from several years of data and including all
                new data as it becomes available),
            - medium_term (approximately last 6 months),
            - short_term (approximately last 4 weeks).
    limit
        The number of artists to return.

    Returns
    -------
    list
        A list of the user's top artists.
    """
    # get user's Spotify ID
    user_id = spotify_get_user_id()
    # get artists IDs from the database
    artists_ids = crud.get_artists_ids()

    # fetch user's top artists from Spotify
    user_top_artists = spotify_get_user_top_artists(
        time_range=time_range,
        limit=limit,
    )

    # get albums IDs from the database
    albums_ids = crud_albums.get_albums_ids()

    for artist in user_top_artists:
        current_artist_id = artist["id"]

        # check if artist is already in the database
        if current_artist_id not in artists_ids:
            # add current artist to the list of artists in the database
            artists_ids.append(current_artist_id)
            crud.insert_artist(
                artist=Artist(**artist),
            )
            # fetch artist's albums from Spotify
            artist_albums_ids = spotify_get_artist_albums_ids(
                artist_id=current_artist_id,
            )
            for album_id in artist_albums_ids:
                if album_id not in albums_ids:
                    album_info = spotify_get_album(
                        album_id=album_id,
                    )
                    crud_albums.insert_album(
                        album=Album.model_validate(album_info),
                    )
                    crud_albums.insert_album_artist(
                        album_id=album_id,
                        artist_id=current_artist_id,
                    )
                    albums_ids.append(album_id)

        # insert artist as top artist for the user
        crud.insert_top_artist_user(
            artist_id=current_artist_id,
            user_id=user_id,
        )

        # fetch related artists from Spotify
        related_artists = spotify_get_related_artists(
            artist_id=current_artist_id,
        )

        for related_artist in related_artists:
            # check if related artist is already in the database
            if related_artist["id"] not in artists_ids:
                # add related artist to the list of artists in the database
                artists_ids.append(related_artist["id"])
                crud.insert_artist(
                    artist=Artist(**related_artist),
                )
            # insert related artist into the database
            crud.insert_related_artist_user(
                artist_id=current_artist_id,
                related_artist_id=related_artist["id"],
            )

    return user_top_artists


def get_random_artist(user_id: str):
    """Get random artists from the database.

    Returns
    -------
    list
        A list of random artists.
    """
    random_artist = crud.get_random_artist(user_id=user_id)
    return random_artist
