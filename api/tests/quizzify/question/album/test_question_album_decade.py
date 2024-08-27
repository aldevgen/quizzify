import unittest

from quizzify.question.album.question_album_decade import QuestionAlbumDecade
from quizzify.question.question_types import AlbumQuestionType


class TestQuestionAlbumDecade(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.album_name = "Wonderful Wonderful"
        self.artist_name = "The Killers"
        self.release_decade = "2010"
        self.correct_answer = self.release_decade
        self.question = QuestionAlbumDecade(
            album_name=self.album_name,
            artist_name=self.artist_name,
            release_decade=self.release_decade,
            answer=self.correct_answer,
        )

    def test_initialization(self):
        """Test initialization of QuestionAlbumArtist."""
        self.assertEqual(self.question.album_name, self.album_name)
        self.assertEqual(self.question.artist_name, self.artist_name)
        self.assertEqual(self.question.correct_answer, self.release_decade)
        self.assertEqual(self.question.question_type, AlbumQuestionType.ALBUM_DECADE)

    def test_display_question(self):
        """Test display_question method of QuestionAlbumArtist."""
        expected_question = (
            f"In which decade was the album '{self.album_name}' released?"
        )
        self.assertEqual(self.question.display_question(), expected_question)
