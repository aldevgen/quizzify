from quizzify.question.abstract_question import AbstractQuestion


class QuestionAlbum(AbstractQuestion):
    """Album question class."""

    def __init__(
        self,
    ) -> None:
        """Album question constructor."""
        super().__init__()

    def get_question(self):
        """Get an album question."""
        pass

    def get_correct_answer(self):
        """Get the correct answer of the album question."""
        pass

    def get_incorrect_answers(self):
        """Get the incorrect answers of the album question."""
        pass

    def get_all_answers(self):
        """Get all answers of the album question."""
        pass
