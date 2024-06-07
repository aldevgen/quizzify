from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import AlbumQuestionType


class QuestionAlbumArtist(AbstractQuestion):
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
        self.question_type = AlbumQuestionType.ALBUM_ARTIST

    def display_question(self):
        """Get an album question."""
        return f"Which artist wrote the '{self.album_name}' album?"
