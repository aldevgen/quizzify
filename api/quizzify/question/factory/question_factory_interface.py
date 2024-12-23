from abc import ABC, abstractmethod

from quizzify.question.abstract_question import AbstractQuestion


class QuestionFactoryInterface(ABC):
    """
    Interface class for question factories.

    Methods
    -------
    create_question(**kwargs)
        Create a question based on the question type.
    """

    @abstractmethod
    def create_question(self, **kwargs) -> AbstractQuestion:
        """
        Create a question based on the question type.

        Parameters
        ----------
        kwargs : dict
            The keyword arguments to create the question.
        """
        pass
