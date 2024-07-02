import unittest
from unittest.mock import patch

from quizzify.question.album.question_album_artist import QuestionAlbumArtist
from quizzify.question.question_types import AlbumQuestionType


class TestQuestionAlbumArtist(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.album_id = "album123"
        self.album_name = "Test Album"
        self.artist_id = "artist123"
        self.artist_name = "Test Artist"
        self.song_id = "song123"
        self.song_name = "Test Song"
        self.answer = "Correct Answer"

        self.question = QuestionAlbumArtist(
            album_id=self.album_id,
            album_name=self.album_name,
            artist_id=self.artist_id,
            artist_name=self.artist_name,
            song_id=self.song_id,
            song_name=self.song_name,
            answer=self.answer,
        )

    def test_initialization(self):
        """Test initialization of QuestionAlbumArtist."""
        self.assertEqual(self.question.album_id, self.album_id)
        self.assertEqual(self.question.album_name, self.album_name)
        self.assertEqual(self.question.artist_id, self.artist_id)
        self.assertEqual(self.question.artist_name, self.artist_name)
        self.assertEqual(self.question.song_id, self.song_id)
        self.assertEqual(self.question.song_name, self.song_name)
        self.assertEqual(self.question.correct_answer, self.answer)
        self.assertEqual(self.question.question_type, AlbumQuestionType.ALBUM_ARTIST)

    def test_display_question(self):
        """Test display_question method."""
        expected_question = f"Which artist wrote the '{self.album_name}' album?"
        self.assertEqual(self.question.display_question(), expected_question)

    @patch("quizzify.crud.artists.get_random_related_artists_name")
    def test_set_incorrect_answers_with_related_artists_in_db(
        self,
        mock_get_random_related_artists_name,
    ):
        """Test set_incorrect_answers when related artists are found in the database."""
        mock_get_random_related_artists_name.return_value = [
            "Artist 1",
            "Artist 2",
            "Artist 3",
        ]

        self.question.set_incorrect_answers()

        mock_get_random_related_artists_name.assert_called_once_with(
            artist_id=self.artist_id,
            nb_artists=3,
        )
        self.assertEqual(
            self.question.incorrect_answers,
            ["Artist 1", "Artist 2", "Artist 3"],
        )


if __name__ == "__main__":
    unittest.main()
