import logging

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.factory.album_question_factory import AlbumQuestionFactory
from quizzify.question.factory.artist_question_factory import ArtistQuestionFactory
from quizzify.question.factory.song_question_factory import SongQuestionFactory
from quizzify.question.question_types import QuestionType

logger = logging.getLogger(__name__)


class QuestionFactory:
    """
    Factory class to create questions.

    Methods
    -------
    create_question(factory_type, **kwargs)
        Create a question based on the factory type.
    """

    @staticmethod
    def create_question(factory_type: QuestionType, **kwargs) -> AbstractQuestion:
        """
        Create a question based on the factory type.

        Parameters
        ----------
        factory_type : QuestionType
            The type of question to create.
        kwargs : dict
            The keyword arguments to create the question.

        Returns
        -------
        AbstractQuestion
            The created question.
        """
        if factory_type == QuestionType.ALBUM.value:
            factory = AlbumQuestionFactory()
        elif factory_type == QuestionType.ARTIST.value:
            factory = ArtistQuestionFactory()
        elif factory_type == QuestionType.SONG.value:
            factory = SongQuestionFactory()
        else:
            raise ValueError("Unvalid factory type")

        question = factory.create_question(**kwargs)
        logger.info(f"Question created: {question.display_question()}")
        logger.info(f"Correct answer: {question.correct_answer}")
        return question
