from quizzify.crud import albums as crud


def get_random_album():
    """Get a random album from the database.

    Returns
    -------
    list
        A list containing a random album.
    """
    random_album = crud.get_random_album()
    return random_album
