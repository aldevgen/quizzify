from quizzify.question.abstract_question import AbstractQuestion


class QuestionSong(AbstractQuestion):
    """Song question class."""

    def __init__(
        self,
        artist_name,
        song_name,
        answer,
    ) -> None:
        """Song question constructor."""
        super().__init__()
        self.artist_name = artist_name
        self.song_name = song_name
        self.correct_answer = answer

    def get_question(self):
        """Get a song question."""
        return f"Who sings '{self.song_name}'?"

    def get_correct_answer(self):
        """Get the correct answer of the song question."""
        pass

    def get_incorrect_answers(self):
        """Get the incorrect answers of the song question."""
        pass

    def get_all_answers(self):
        """Get all answers of the song question."""
        pass
