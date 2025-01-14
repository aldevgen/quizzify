import os

import requests  # type: ignore[import-untyped]
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("LASTFM_API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"
USER_AGENT = "quizzify"


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
    headers = {"user-agent": USER_AGENT}
    url = BASE_URL

    # Add API key and format to the payload
    payload = {
        "method": "artist.getsimilar",
        "artist": artist_name,
        "autocorrect": 1,
        "limit": limit,
        "api_key": API_KEY,
        "format": "json",
    }

    raw_response = requests.get(url, headers=headers, params=payload, timeout=120)
    if raw_response.status_code == 200:
        response = raw_response.json()
        related_artists = []
        lastfm_similar_artists = response["similarartists"]["artist"]
        for artist in lastfm_similar_artists:
            related_artists.append(artist["name"])
        return related_artists
