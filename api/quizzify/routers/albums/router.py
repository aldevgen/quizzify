from fastapi import APIRouter

from quizzify.routers.albums import service
from quizzify.spotify.spotify_requests import spotify_get_user_id

router = APIRouter()


@router.get(
    path="/random",
    summary="Return a random album from Spotify",
    description="Return random album from the database.",
)
async def get_random_album():
    """
    Fetch a random album from user's listening top songs or artists.

    Returns
    -------
    list
        A random album from user's albums.
    """
    user_id = spotify_get_user_id()
    random_album = service.get_random_album(user_id=user_id)
    return random_album
