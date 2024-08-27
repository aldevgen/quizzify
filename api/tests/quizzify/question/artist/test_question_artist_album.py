import unittest

from quizzify.question.artist.question_artist_album import QuestionArtistAlbum
from quizzify.question.question_types import ArtistQuestionType


class TestQuestionArtistAlbum(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.album_name = "Wonderful Wonderful"
        self.artist_id = "0C0XlULifJtAgn6ZNCW2eu"
        self.artist_name = "The Killers"
        self.correct_answer = self.album_name
        self.question = QuestionArtistAlbum(
            album_name=self.album_name,
            artist_id=self.artist_id,
            artist_name=self.artist_name,
            answer=self.correct_answer,
        )

    def test_initialization(self):
        """Test initialization of QuestionArtistAlbum."""
        self.assertEqual(self.question.album_name, self.album_name)
        self.assertEqual(self.question.artist_id, self.artist_id)
        self.assertEqual(self.question.artist_name, self.artist_name)
        self.assertEqual(self.question.correct_answer, self.album_name)
        self.assertEqual(self.question.question_type, ArtistQuestionType.ARTIST_ALBUM)

    def test_display_question(self):
        """Test display_question method of QuestionArtistAlbum."""
        expected_question = f"Which album is from the artist {self.artist_name}?"
        self.assertEqual(self.question.display_question(), expected_question)
