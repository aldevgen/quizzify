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
        self.album_name = album_name
        self.artist_name = artist_name
        self.release_decade = release_decade
        self.correct_answer = answer
        self.question_type = AlbumQuestionType.ALBUM_DECADE

    def display_question(self):
        """Get an album question."""
        return f"In which decade was the album '{self.album_name}' released?"
