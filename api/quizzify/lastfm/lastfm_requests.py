# cf https://www.last.fm/api/authentication

# 1. Request authorization from the user
# http://www.last.fm/api/auth/?api_key=xxx
# 2. Redirect the user back to your site
# http://www.yourwebsite.com/auth?token=xxx
# 3. Authentication Tokens
# api_key: (Required) Your API key.
# token: (Required) The authentication token received from step 1.
# api_sig: (Required) A 32-character hexadecimal md5 hash of the token+shared secret.
# 4. Session Key
# api_key: (Required) Your API key.
# token: (Required) A 32-character ASCII hexadecimal MD5 hash of the last.fm password.
# username: (Required) The last.fm username.

import os

import requests  # type: ignore[import-untyped]
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("LASTFM_API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"
USER_AGENT = "quizzify"


def lastfm_get_similar_artists(artist_name):
    """Get similar artists from LastFM.

    Parameters
    ----------
    artist_name : str
        The name of the artist to get similar artists for.

    Returns
    -------
    list
        A list of similar artists.
    """
    headers = {"user-agent": USER_AGENT}
    url = BASE_URL
    artist_name = artist_name.replace(" ", "+")

    # Add API key and format to the payload
    payload = {
        "method": "artist.getsimilar",
        "artist": artist_name,
        "api_key": API_KEY,
        "format": "json",
    }

    raw_response = requests.get(url, headers=headers, params=payload, timeout=120)
    if raw_response.status_code == 200:
        response = raw_response.json()
        related_artists = []
        for artist in response["similarartists"]["artist"]:
            related_artists.append(artist["name"])
        return related_artists
