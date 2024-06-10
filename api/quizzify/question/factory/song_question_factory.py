import logging
import random

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.factory.question_factory_interface import (
    QuestionFactoryInterface,
)
from quizzify.question.question_types import SongQuestionType
from quizzify.question.song.question_song_album import QuestionSongAlbum
from quizzify.question.song.question_song_artist import QuestionSongArtist

logger = logging.getLogger(__name__)


class SongQuestionFactory(QuestionFactoryInterface):
    """
    Factory class to create song questions.

    Methods
    -------
    create_question(**kwargs)
        Create a question based on the song question type.
    """

    @staticmethod
    def create_question(**kwargs) -> AbstractQuestion:
        """
        Create a question based on the song question type.

        Parameters
        ----------
        kwargs : dict
            The keyword arguments to create the question.

        Returns
        -------
        AbstractQuestion
            The created song question.
        """
        question_types = SongQuestionType.get_items()
        chosen_question = random.choice(question_types)
        logger.info(f"Creating question {chosen_question.upper()} type.")

        if chosen_question == SongQuestionType.SONG_ARTIST.value:
            artist_id = kwargs.get("artist_id")
            artist_name = kwargs.get("artist_name")
            song_id = kwargs.get("song_id")
            song_name = kwargs.get("song_name")
            return QuestionSongArtist(
                artist_id=artist_id,
                artist_name=artist_name,
                song_id=song_id,
                song_name=song_name,
                answer=artist_name,
            )

        elif chosen_question == SongQuestionType.SONG_ALBUM.value:
            song_name = kwargs.get("song_name")
            album_name = kwargs.get("album_name")
            artist_name = kwargs.get("artist_name")
            return QuestionSongAlbum(
                song_name=song_name,
                artist_name=artist_name,
                album_name=album_name,
                answer=album_name,
            )

        else:
            raise ValueError("Unknown song question type")
