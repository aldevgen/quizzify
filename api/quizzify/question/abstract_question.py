from abc import ABC, abstractmethod


class AbstractQuestion(ABC):
    """Abstract class for questions."""

    def __init__(self):
        """Abstract class for questions."""
        pass

    @abstractmethod
    def get_question(self):
        """Abstract method to get a question."""
        pass

    @abstractmethod
    def get_correct_answer(self):
        """Abstract method to get the correct answer."""
        pass

    @abstractmethod
    def get_incorrect_answers(self):
        """Abstract method to get the incorrect answers."""
        pass

    @abstractmethod
    def get_all_answers(self):
        """Abstract method to get all answers."""
        pass
