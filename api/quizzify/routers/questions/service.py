import logging
import random

from quizzify.crud import albums as crud_albums
from quizzify.crud import artists as crud_artists
from quizzify.crud import songs as crud_songs
from quizzify.question.factory.question_factory import QuestionFactory
from quizzify.question.question_types import QuestionType
from quizzify.spotify.spotify_requests import spotify_get_user_id

logger = logging.getLogger(__name__)


def create_question():
    """Create a random question.

    Returns
    -------
    dict
        A random question.
    """
    # instantiate the QuestionFactory class
    qf = QuestionFactory()
    # get all the question types available
    question_types = QuestionType.get_items()
    # choose a random question type
    factory_type = random.choice(question_types)
    logger.info(f"Creating question {factory_type.upper()} type.")

    # get the user's Spotify ID
    user_id = spotify_get_user_id()
    # create a question based on the chosen question type
    question = None
    if factory_type == QuestionType.ALBUM.value:
        album_info = crud_albums.get_random_album(user_id=user_id)
        question = qf.create_question(
            factory_type=factory_type,
            album_id=album_info["album_id"],
            album_name=album_info["album_name"],
            artist_id=album_info["artist_id"],
            artist_name=album_info["artist_name"],
            album_year=album_info["release_year"],
            release_decade=album_info["release_decade"],
        )
    elif factory_type == QuestionType.ARTIST.value:
        artist_info = crud_artists.get_random_artist_album(user_id=user_id)
        question = qf.create_question(
            factory_type=factory_type,
            artist_id=artist_info["artist_id"],
            artist_name=artist_info["artist_name"],
            album_name=artist_info["album_name"],
            album_id=artist_info["album_id"],
            genres=artist_info["genres"],
        )
    elif factory_type == QuestionType.SONG.value:
        song_info = crud_songs.get_random_song(user_id=user_id)
        question = qf.create_question(
            factory_type=factory_type,
            album_id=song_info["album_id"],
            album_name=song_info["album_name"],
            artist_id=song_info["artist_id"],
            artist_name=song_info["artist_name"],
            song_id=song_info["song_id"],
            song_name=song_info["song_name"],
        )
    return question.get_question()
