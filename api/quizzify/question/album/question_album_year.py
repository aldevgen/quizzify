from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import AlbumQuestionType
from quizzify.utils.helpers import generate_random_years


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
        """Set incorrect answers for the album question.

        This method generates 3 random years around the correct answer within the
        range limit of more or less 20 years.
        """
        range_limit = 20
        self.incorrect_answers = generate_random_years(
            year=int(self.correct_answer),
            range_limit=range_limit,
            num_years=3,
        )
