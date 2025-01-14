import random
from abc import ABC, abstractmethod
from typing import List, Optional


class AbstractQuestion(ABC):
    """Abstract class for questions."""

    def __init__(self) -> None:
        """Abstract question constructor."""
        self.correct_answer: Optional[str] = None
        self.incorrect_answers: List[str] = []

    @abstractmethod
    def display_question(self):
        """Abstract method to get a question."""
        pass

    def get_correct_answer(self):
        """Abstract method to get the correct answer."""
        return self.correct_answer

    def get_incorrect_answers(self) -> List:
        """Abstract method to get the incorrect answers."""
        if not self.incorrect_answers:
            self.set_incorrect_answers()
        return self.incorrect_answers

    @abstractmethod
    def set_incorrect_answers(self):
        """Set the incorrect answers."""
        pass

    def get_all_answers(self) -> List:
        """Abstract method to get all answers."""
        if not self.incorrect_answers:
            self.set_incorrect_answers()
        all_answers = [self.correct_answer] + self.incorrect_answers
        random.shuffle(all_answers)
        return all_answers

    def get_question(self):
        """Get a song question."""
        return {
            "question": self.display_question(),
            "question_type": self.question_type,
            "correct_answer": self.get_correct_answer(),
            "incorrect_answers": self.get_incorrect_answers(),
            "all_answers": self.get_all_answers(),
        }
