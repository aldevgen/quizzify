from fastapi import APIRouter

from quizzify.routers.albums import service

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
    random_album = service.get_random_album()
    return random_album
