import unittest
from unittest.mock import patch

from quizzify.question.abstract_question import AbstractQuestion


class TestAbstractQuestion(unittest.TestCase):
    @patch.multiple(AbstractQuestion, __abstractmethods__=set())
    def setUp(self):
        self.question = AbstractQuestion()

    def test_display_question(self):
        """Test display_question method."""
        self.assertEqual(self.question.display_question(), None)

    def test_get_correct_answer(self):
        """Test get_correct_answer method."""
        self.assertEqual(self.question.get_correct_answer(), None)

    def test_get_incorrect_answers(self):
        """Test get_incorrect_answers method."""
        self.assertEqual(self.question.get_incorrect_answers(), [])
        self.assertEqual(self.question.incorrect_answers, [])

    def test_get_all_answers(self):
        """Test get_all_answers method."""
        self.assertEqual(self.question.get_all_answers(), [None])
        self.assertEqual(self.question.incorrect_answers, [])

    def test_get_question(self):
        """Test get_question method."""
        self.assertEqual(
            self.question.get_question(),
            {
                "question": None,
                "question_type": None,
                "correct_answer": None,
                "incorrect_answers": [],
                "all_answers": [None],
            },
        )
