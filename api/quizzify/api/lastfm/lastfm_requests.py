import os

import requests  # type: ignore[import-untyped]
from dotenv import load_dotenv

from quizzify.utils.constants import LASTFM_BASE_URL, LASTFM_USER_AGENT

load_dotenv()

API_KEY = os.environ.get("LASTFM_API_KEY")


def lastfm_get_similar_artists(
    artist_name: str,
    limit: int = 5,
):
    """Get similar artists from LastFM.

    Parameters
    ----------
    artist_name : str
        The name of the artist to get similar artists for.
    limit : int, optional
        The number of similar artists to fetch.

    Returns
    -------
    list
        A list of similar artists.
    """
    headers = {"user-agent": LASTFM_USER_AGENT}

    # Add API key and format to the payload
    payload = {
        "method": "artist.getsimilar",
        "artist": artist_name,
        "autocorrect": 1,
        "limit": limit,
        "api_key": API_KEY,
        "format": "json",
    }

    raw_response = requests.get(
        LASTFM_BASE_URL,
        headers=headers,
        params=payload,
        timeout=120,
    )
    if raw_response.status_code == 200:
        response = raw_response.json()
        related_artists = []
        lastfm_similar_artists = response["similarartists"]["artist"]
        for artist in lastfm_similar_artists:
            related_artists.append(artist["name"])
        return related_artists
