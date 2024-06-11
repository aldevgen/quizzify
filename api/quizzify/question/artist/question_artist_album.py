from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import ArtistQuestionType


class QuestionArtistAlbum(AbstractQuestion):
    """Artist question class."""

    def __init__(self, artist_name, album_name, answer) -> None:
        """Artist question constructor."""
        super().__init__()
        self.question_type = ArtistQuestionType.ARTIST_ALBUM
        self.artist_name = artist_name
        self.album_name = album_name
        self.correct_answer = answer

    def display_question(self) -> str:
        """Get an artist question."""
        return f"Which album is from the artist {self.artist_name}?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the artist question."""
        pass
