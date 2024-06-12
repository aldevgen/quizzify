import logging
import random

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.artist.question_artist_album import QuestionArtistAlbum
from quizzify.question.factory.question_factory_interface import (
    QuestionFactoryInterface,
)
from quizzify.question.question_types import ArtistQuestionType

logger = logging.getLogger(__name__)


class ArtistQuestionFactory(QuestionFactoryInterface):
    """
    Factory class to create artist questions.

    Methods
    -------
    create_question(**kwargs)
        Create a question based on the artist question type.
    """

    @staticmethod
    def create_question(**kwargs) -> AbstractQuestion:
        """
        Create a question based on the artist question type.

        Parameters
        ----------
        kwargs : dict
            The keyword arguments to create the question.

        Returns
        -------
        AbstractQuestion
            The created artist question.

        """
        question_types = ArtistQuestionType.get_items()
        chosen_question = random.choice(question_types)
        logger.info(f"Creating question {chosen_question.upper()} type.")

        return QuestionArtistAlbum(
            artist_id=kwargs.get("artist_id"),
            album_name=kwargs.get("album_name"),
            artist_name=kwargs.get("artist_name"),
            answer=kwargs.get("album_name"),
        )
