from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import SongQuestionType


class QuestionSongAlbum(AbstractQuestion):
    """Song question class."""

    def __init__(
        self,
        artist_name,
        album_name,
        song_name,
        answer,
    ) -> None:
        """Song question constructor."""
        super().__init__()
        self.artist_name = artist_name
        self.album_name = album_name
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = SongQuestionType.SONG_ALBUM

    def display_question(self):
        """Get a song question."""
        return f"In which album is the song '{self.song_name}' in?"
