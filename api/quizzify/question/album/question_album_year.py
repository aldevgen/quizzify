import random
from datetime import datetime

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import AlbumQuestionType


class QuestionAlbumYear(AbstractQuestion):
    """Album question class."""

    def __init__(
        self,
        album_name,
        artist_name,
        song_name,
        answer,
    ) -> None:
        """Album question constructor."""
        super().__init__()
        self.album_name = album_name
        self.artist_name = artist_name
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = AlbumQuestionType.ALBUM_YEAR

    def display_question(self) -> str:
        """Get an album question."""
        return f"In which year was the album '{self.album_name}' released?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the album question."""
        range_limit = 20
        year = int(self.correct_answer)
        current_year = datetime.now().year
        max_year = min(current_year, year + range_limit)
        min_year = year - range_limit
        incorrect_answers = [
            str(random.randint(min_year, max_year)) for _ in range(0, 3)
        ]
        self.incorrect_answers = incorrect_answers
