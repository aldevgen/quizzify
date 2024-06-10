from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import SongQuestionType


class QuestionSongArtist(AbstractQuestion):
    """Song question class."""

    def __init__(
        self,
        artist_id,
        artist_name,
        song_id,
        song_name,
        answer,
    ) -> None:
        """Song question constructor."""
        super().__init__()
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_id = song_id
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = SongQuestionType.SONG_ARTIST

    def display_question(self):
        """Get a song question."""
        return f"Which artist sings '{self.song_name}'?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the song question."""
        pass
