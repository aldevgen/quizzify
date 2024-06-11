import random
from typing import List

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import AlbumQuestionType


class QuestionAlbumDecade(AbstractQuestion):
    """Album question class."""

    def __init__(
        self,
        album_name,
        artist_name,
        release_decade,
        answer,
    ) -> None:
        """Album question constructor."""
        super().__init__()
        self.album_name: str = album_name
        self.artist_name: str = artist_name
        self.release_decade: str = release_decade
        self.correct_answer: str = answer
        self.question_type = AlbumQuestionType.ALBUM_DECADE
        self.all_decades: List[str] = [
            "1960",
            "1970",
            "1980",
            "1990",
            "2000",
            "2010",
            "2020",
        ]
        self.all_decades.remove(self.correct_answer)

    def display_question(self) -> str:
        """Output the album question.

        Returns
        -------
        str
            The album question formatted as a string.
        """
        return f"In which decade was the album '{self.album_name}' released?"

    def set_incorrect_answers(self) -> None:
        """Set incorrect answers for the album question.

        This method randomly selects 3 decades to be the incorrect answers from
        the list of all decades, excluding the correct answer.
        """
        self.incorrect_answers = random.sample(self.all_decades, k=3)
