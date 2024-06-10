from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.artist.question_artist_album import QuestionArtistAlbum
from quizzify.question.factory.question_factory_interface import (
    QuestionFactoryInterface,
)


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
        album_name = kwargs.get("album_name")
        artist_name = kwargs.get("artist_name")
        return QuestionArtistAlbum(
            album_name=album_name,
            artist_name=artist_name,
            answer=album_name,
        )
