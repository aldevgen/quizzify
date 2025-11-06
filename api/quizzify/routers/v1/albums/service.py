from quizzify.crud import albums as crud


def get_top_albums(user_id: str):
    """Get top albums from the database.

    Parameters
    ----------
    user_id : str
        The user's Spotify ID.

    Returns
    -------
    list
        Top albums from the user's albums.
    """
    top_albums = crud.get_top_albums(user_id=user_id)
    return top_albums


def get_random_album(user_id: str):
    """Get a random album from the database.

    Returns
    -------
    list
        A list containing a random album.
    """
    random_album = crud.get_random_album(user_id=user_id)
    return random_album
