import logging
import random

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.album.question_album_artist import QuestionAlbumArtist
from quizzify.question.album.question_album_decade import QuestionAlbumDecade
from quizzify.question.album.question_album_year import QuestionAlbumYear
from quizzify.question.factory.question_factory_interface import (
    QuestionFactoryInterface,
)
from quizzify.question.question_types import AlbumQuestionType

logger = logging.getLogger(__name__)


class AlbumQuestionFactory(QuestionFactoryInterface):
    """
    Factory class to create album questions.

    Methods
    -------
    create_question(**kwargs)
        Create a question based on the album question type.
    """

    @staticmethod
    def create_question(**kwargs) -> AbstractQuestion:
        """
        Create a question based on the album question type.

        Parameters
        ----------
        kwargs : dict
            The keyword arguments to create the question.
        """
        question_types = AlbumQuestionType.get_items()
        chosen_question = random.choice(question_types)
        logger.info(f"Creating question {chosen_question.upper()} type.")

        question = None

        if chosen_question == AlbumQuestionType.ALBUM_YEAR.value:
            album_name = kwargs.get("album_name")
            artist_name = kwargs.get("artist_name")
            song_name = kwargs.get("song_name")
            album_year = kwargs.get("album_year")
            question = QuestionAlbumYear(
                album_name=album_name,
                artist_name=artist_name,
                song_name=song_name,
                answer=album_year,
            )
        elif chosen_question == AlbumQuestionType.ALBUM_ARTIST.value:
            question = QuestionAlbumArtist(
                album_id=kwargs.get("album_id"),
                album_name=kwargs.get("album_name"),
                artist_id=kwargs.get("artist_id"),
                artist_name=kwargs.get("artist_name"),
                song_id=kwargs.get("song_id"),
                song_name=kwargs.get("song_name"),
                answer=kwargs.get("artist_name"),
            )
        elif chosen_question == AlbumQuestionType.ALBUM_DECADE.value:
            album_name = kwargs.get("album_name")
            artist_name = kwargs.get("artist_name")
            release_decade = kwargs.get("release_decade")
            question = QuestionAlbumDecade(
                album_name=album_name,
                artist_name=artist_name,
                release_decade=release_decade,
                answer=release_decade,
            )
        return question
