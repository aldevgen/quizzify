import unittest

from quizzify.question.album.question_album_year import QuestionAlbumYear
from quizzify.question.question_types import AlbumQuestionType


class TestQuestionAlbumYear(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.album_name = "Wonderful Wonderful"
        self.artist_name = "The Killers"
        self.release_year = "2010"
        self.correct_answer = self.release_year
        self.question = QuestionAlbumYear(
            album_name=self.album_name,
            artist_name=self.artist_name,
            answer=self.correct_answer,
        )

    def test_initialization(self):
        """Test initialization of QuestionAlbumYear."""
        self.assertEqual(self.question.album_name, self.album_name)
        self.assertEqual(self.question.artist_name, self.artist_name)
        self.assertEqual(self.question.correct_answer, self.release_year)
        self.assertEqual(self.question.question_type, AlbumQuestionType.ALBUM_YEAR)

    def test_display_question(self):
        """Test display_question method of QuestionAlbumYear."""
        expected_question = f"In which year was the album '{self.album_name}' released?"
        self.assertEqual(self.question.display_question(), expected_question)
