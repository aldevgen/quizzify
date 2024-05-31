from quizzify.question.abstract_question import AbstractQuestion


class QuestionArtist(AbstractQuestion):
    """Artist question class."""

    def __init__(self) -> None:
        """Artist question constructor."""
        super().__init__()

    def get_question(self):
        """Get an artist question."""
        pass

    def get_correct_answer(self):
        """Get the correct answer of the artist question."""
        pass

    def get_incorrect_answers(self):
        """Get the incorrect answers of the artist question."""
        pass

    def get_all_answers(self):
        """Get all answers of the artist question."""
        pass
