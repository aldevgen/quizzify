import logging
import os

import requests  # type: ignore[import-untyped]
from dotenv import load_dotenv
from fastapi import HTTPException

from quizzify.crud import albums as crud_albums
from quizzify.crud import artists as crud_artists
from quizzify.crud import songs as crud_songs
from quizzify.spotify.spotify_headers import spotify_headers
from quizzify.spotify.spotify_requests import (
    spotify_get_album,
    spotify_get_artist,
    spotify_get_related_artists,
    spotify_get_user_id,
)
from quizzify.utils.schemas import Album, Artist, Song, TimeRange

# load environment variables
load_dotenv()
# define base URL for Spotify API
SPOTIFY_BASE_URL = os.environ.get("SPOTIFY_BASE_URL")

logger = logging.getLogger(__name__)


def get_top_songs(
    time_range: TimeRange,
    limit: int,
):
    """Get the user's top songs from Spotify.

    Parameters
    ----------
    time_range : TimeRange
        The time range for the top songs.
    limit : int
        The number of songs to fetch (the maximum is set to 50 by the Spotify API).

    Returns
    -------
    list
        A list of the user's top songs.
    """
    headers = spotify_headers()
    api_url = (
        f"{SPOTIFY_BASE_URL}/me/top/tracks?time_range={time_range.value}&limit={limit}"
    )
    response = requests.get(
        api_url,
        headers=headers,
        timeout=120,
    )

    if response.status_code == 200:
        raw_top_songs = response.json()["items"]
        top_songs = []

        # get albums, artists and songs IDs from the database
        albums_ids = crud_albums.get_albums_ids()
        artists_ids = crud_artists.get_artists_ids()
        song_ids = crud_songs.get_songs_ids()

        # get user's Spotify ID
        user_id = spotify_get_user_id()

        for song in raw_top_songs:
            for artist in song["artists"]:
                # insert artist into database
                current_artist_id = artist["id"]
                if current_artist_id not in artists_ids:
                    # add artist ID to the list of artists already known
                    artists_ids.append(current_artist_id)

                    # get artist info and insert it into artists table
                    artist_info = spotify_get_artist(current_artist_id)
                    crud_artists.insert_artist(
                        artist=Artist.model_validate(artist_info),
                    )
                    # insert artist into user's top artists
                    crud_artists.insert_top_artist_user(
                        artist_id=current_artist_id,
                        user_id=user_id,
                    )

                    # fetch related artists from Spotify
                    related_artists = spotify_get_related_artists(
                        artist_id=current_artist_id,
                    )

                    for related_artist in related_artists:
                        # check if related artist is already in the database
                        related_artist_id = related_artist["id"]
                        if related_artist_id not in artists_ids:
                            # add related artist to the list of artists in the database
                            artists_ids.append(related_artist_id)
                            crud_artists.insert_artist(
                                artist=Artist.model_validate(related_artist),
                            )
                            # insert artist as top artist for the user
                            crud_artists.insert_related_artist_user(
                                related_artist_id=related_artist_id,
                                artist_id=current_artist_id,
                            )

                # get artist details
                artists_info = [
                    {"id": artist["id"], "name": artist["name"]}
                    for artist in song["artists"]
                ]

                # get album details
                current_album_id = song["album"]["id"]
                # insert album into database if it is not already there
                if current_album_id not in albums_ids:
                    albums_ids.append(current_album_id)

                    # get album details
                    album_info = spotify_get_album(current_album_id)
                    # insert album info
                    crud_albums.insert_album(
                        album=Album.model_validate(album_info),
                    )
                    # insert album into artist's albums
                    crud_albums.insert_album_artist(
                        album_id=current_album_id,
                        artist_id=current_artist_id,
                    )
                    # insert user
                    crud_albums.insert_top_album_user(
                        album_id=current_album_id,
                        user_id=user_id,
                    )

                    # insert song info into the database if it is not already there
                    current_song_id = song["id"]
                    # get song details
                    song_info = {
                        "id": current_song_id,
                        "name": song["name"],
                        "popularity": song["popularity"],
                        "duration_ms": song["duration_ms"],
                        "track_number": song["track_number"],
                        "album_id": song["album"]["id"],
                        "artist_id": artist["id"],
                    }
                    # insert song into database if it is not already there
                    if current_song_id not in song_ids:
                        song_ids.append(current_song_id)
                        crud_songs.insert_song(song=Song.model_validate(song_info))

                    # insert song into user's top songs
                    crud_songs.insert_song_user(
                        song_id=current_song_id,
                        user_id=user_id,
                    )

                    # create a dictionary with the song, artist and album details
                    current_song = {
                        "song": song_info,
                        "artists": artists_info,
                        "album": album_info,
                    }
                    top_songs.append(current_song)

        return top_songs
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to retrieve top songs",
        )


def get_random_song(user_id: str):
    """Get random songs from the database.

    Returns
    -------
    list
        A list of random songs.
    """
    random_song = crud_songs.get_random_song(user_id=user_id)
    return random_song
