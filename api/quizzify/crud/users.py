import logging
from uuid import UUID

from dotenv import load_dotenv
from psycopg2 import sql

from quizzify.db.query_executor import QueryExecutor

load_dotenv()
logger = logging.getLogger(__name__)


def create_spotify_user(
    spotify_id: UUID,
    spotify_username: str,
    spotify_email: str,
    spotify_image_url: str,
    spotify_uri: str,
):
    """Register a user by adding its Spotify information in the database.

    Parameters
    ----------
    spotify_id : UUID
        The user's unique identifier.
    spotify_username : str
        The user's Spotify username.
    spotify_email : str
        The user's Spotify email.
    spotify_image_url : str
        The user's Spotify image URL.
    spotify_uri : str
        The user's Spotify URI.
    """
    query = sql.SQL(
        "INSERT INTO users_spotify "
        "(spotify_id, spotify_username, spotify_email, spotify_image_url, "
        "spotify_uri) "
        "VALUES"
        "("
        "%(spotify_id)s, %(spotify_username)s, %(spotify_email)s, "
        "%(spotify_image_url)s, %(spotify_uri)s"
        ");"
    )
    variables = {
        "spotify_id": spotify_id,
        "spotify_username": spotify_username,
        "spotify_email": spotify_email,
        "spotify_image_url": spotify_image_url,
        "spotify_uri": spotify_uri,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables, fetch=False)
    logger.info(f"Spotify user {spotify_username} successfully created.")


def create_user(
    user_id: str,
    username: str,
    email: str,
    hashed_pwd: str,
):
    """
    Register a user in the quizz and add its information in the database.

    Parameters
    ----------
    user_id : str
        The user's unique identifier.
    username : str
        The username for the new account.
    email : str
        The user's email.
    hashed_pwd : str
        The hashed password for the new account.
    """
    query = sql.SQL(
        "INSERT INTO users_quizzify "
        "(user_id, username, email, hashed_pwd) "
        "VALUES"
        "(%(user_id)s, %(username)s, %(email)s, %(hashed_pwd)s );"
    )
    variables = {
        "user_id": user_id,
        "username": username,
        "email": email,
        "hashed_pwd": hashed_pwd,
    }
    with QueryExecutor() as executor:
        executor.execute(query, variables, fetch=False)
    logger.info(f"User {username} successfully created.")


def get_user_email(
    email: str,
):
    """Check if the email is already in use.

    Parameters
    ----------
    email : str
        The user's email.

    Returns
    -------
    tuple
        The user's information.
    """
    query = sql.SQL("SELECT email FROM users_quizzify WHERE email = %(email)s;")
    variables = {"email": email}
    with QueryExecutor() as executor:
        user_info = executor.execute(query, variables, fetch=True, one=False)
    return user_info


def get_user_by_email(
    email: str,
):
    """Check if the email corresponds to a user.

    Parameters
    ----------
    email : str
        The user's email.

    Returns
    -------
    tuple
        The user's email and hashed password.
    """
    query = sql.SQL(
        "SELECT username, email, hashed_pwd "
        "FROM users_quizzify "
        "WHERE email = %(email)s;"
    )
    variables = {"email": email}
    with QueryExecutor() as executor:
        user_info = executor.execute(query, variables, fetch=True, one=True)
        if user_info is not None:
            user_name = user_info["username"]
            user_email = user_info["email"]
            user_pwd = user_info["hashed_pwd"]
            return user_name, user_email, user_pwd
        else:
            return None, None, None


def get_user_by_spotify_id(
    spotify_id: str,
):
    """Get a user by its Spotify ID.

    Parameters
    ----------
    spotify_id : str
        The user's Spotify ID.

    Returns
    -------
    str
        The user's Spotify ID.
    """
    query = sql.SQL(
        "SELECT spotify_id FROM users_spotify WHERE spotify_id = %(spotify_id)s;"
    )
    variables = {"spotify_id": spotify_id}
    with QueryExecutor() as executor:
        user_email = executor.execute(query, variables, fetch=True)
    return user_email


def get_user_by_username(
    username: str,
):
    """Get a user by its username.

    Parameters
    ----------
    username : str
        The user's username.

    Returns
    -------
    str
        The user's username.
    """
    query = sql.SQL(
        "SELECT username FROM users_quizzify WHERE username = %(username)s;"
    )
    variables = {"username": username}
    with QueryExecutor() as executor:
        user_email = executor.execute(query, variables, fetch=True)
    return user_email
