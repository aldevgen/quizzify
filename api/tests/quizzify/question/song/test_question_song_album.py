import unittest

from quizzify.question.question_types import SongQuestionType
from quizzify.question.song.question_song_album import QuestionSongAlbum


class TestQuestionSongAlbum(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.album_id = "72ZfMxLCPG8mlWC0TXfZQi"
        self.album_name = "Wonderful Wonderful"
        self.artist_id = "0C0XlULifJtAgn6ZNCW2eu"
        self.artist_name = "The Killers"
        self.song_id = "5aWhs651KYM26HYM16kRdk"
        self.song_name = "The Man"
        self.correct_answer = self.album_name

        self.question = QuestionSongAlbum(
            album_id=self.album_id,
            album_name=self.album_name,
            artist_id=self.artist_id,
            artist_name=self.artist_name,
            song_id=self.song_id,
            song_name=self.song_name,
            answer=self.correct_answer,
        )

    def test_initialization(self):
        """Test initialization of QuestionSongAlbum."""
        self.assertEqual(self.question.album_id, self.album_id)
        self.assertEqual(self.question.album_name, self.album_name)
        self.assertEqual(self.question.artist_id, self.artist_id)
        self.assertEqual(self.question.artist_name, self.artist_name)
        self.assertEqual(self.question.song_id, self.song_id)
        self.assertEqual(self.question.song_name, self.song_name)
        self.assertEqual(self.question.correct_answer, self.album_name)
        self.assertEqual(self.question.question_type, SongQuestionType.SONG_ALBUM)

    def test_display_question(self):
        """Test display_question method of QuestionSongAlbum."""
        expected_question = (
            f"In which album does {self.artist_name} sing '{self.song_name}'?"
        )
        self.assertEqual(self.question.display_question(), expected_question)
