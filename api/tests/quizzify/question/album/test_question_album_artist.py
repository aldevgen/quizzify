import unittest

# from unittest.mock import MagicMock, patch
from unittest.mock import patch

# from quizzify.crud import artists as crud_artists
from quizzify.question.album.question_album_artist import QuestionAlbumArtist
from quizzify.question.question_types import AlbumQuestionType

# from quizzify.spotify.spotify_requests import spotify_get_related_artists
# from quizzify.utils.schemas import Artist


class TestQuestionAlbumArtist(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.album_id = "72ZfMxLCPG8mlWC0TXfZQi"
        self.album_name = "Wonderful Wonderful"
        self.artist_id = "0C0XlULifJtAgn6ZNCW2eu"
        self.artist_name = "The Killers"
        self.song_id = "5aWhs651KYM26HYM16kRdk"
        self.song_name = "The Man"

        self.question = QuestionAlbumArtist(
            album_id=self.album_id,
            album_name=self.album_name,
            artist_id=self.artist_id,
            artist_name=self.artist_name,
            song_id=self.song_id,
            song_name=self.song_name,
            answer=self.artist_name,
        )

        self.related_artists = [
            {
                "id": "related_artist_1",
                "name": "Related Artist 1",
                "popularity": 80,
                "genres": ["pop"],
                "followers": 1000,
                "image_url": "http://image.url/1",
            },
            {
                "id": "related_artist_2",
                "name": "Related Artist 2",
                "popularity": 70,
                "genres": ["rock"],
                "followers": 500,
                "image_url": "http://image.url/2",
            },
        ]
        self.existing_artist_ids = ["existing_artist_1"]

    def test_initialization(self):
        """Test initialization of QuestionAlbumArtist."""
        self.assertEqual(self.question.album_id, self.album_id)
        self.assertEqual(self.question.album_name, self.album_name)
        self.assertEqual(self.question.artist_id, self.artist_id)
        self.assertEqual(self.question.artist_name, self.artist_name)
        self.assertEqual(self.question.song_id, self.song_id)
        self.assertEqual(self.question.song_name, self.song_name)
        self.assertEqual(self.question.correct_answer, self.artist_name)
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

    # @patch("quizzify.spotify.spotify_headers")
    # @patch("quizzify.spotify.spotify_token_manager.SpotifyTokenManager")
    # @patch("quizzify.spotify.spotify_requests.spotify_get_related_artists")
    # @patch("quizzify.crud.artists.get_artists_ids")
    # @patch("quizzify.crud.artists.insert_artist")
    # @patch("quizzify.crud.artists.insert_related_artist_user")
    # @patch(
    #     "quizzify.spotify.spotify_token_manager.SpotifyTokenManager",
    #     "3",
    # )
    # def test_set_incorrect_answers_with_related_artists_spotify(
    #     self,
    #     mock_spotify_headers,
    #     mock_spotify_token_manager,
    #     mock_insert_related_artist_user,
    #     mock_insert_artist,
    #     mock_get_artists_ids,
    #     mock_spotify_get_related_artists,
    # ):
    #     # Arrange
    #     mock_spotify_get_related_artists.return_value = self.related_artists
    #     mock_get_artists_ids.return_value = self.existing_artist_ids
    #     mock_spotify_headers.return_value = {"Authorization": "Bearer valid_token"}
    #
    #     # Mock the SpotifyTokenManager to return a valid token
    #     mock_token_manager_instance = MagicMock()
    #     mock_token_manager_instance.access_token = "valid_token"
    #     mock_spotify_token_manager.return_value = mock_token_manager_instance
    #
    #     # Act
    #     related_artists = spotify_get_related_artists(artist_id=self.artist_id)
    #     artists_ids = crud_artists.get_artists_ids()
    #     for related_artist in related_artists:
    #         related_artist_id = related_artist["id"]
    #         if related_artist_id not in artists_ids:
    #             artists_ids.append(related_artist_id)
    #             crud_artists.insert_artist(
    #                 artist=Artist.model_validate(related_artist),
    #             )
    #             crud_artists.insert_related_artist_user(
    #                 related_artist_id=related_artist_id,
    #                 artist_id=self.artist_id,
    #             )
    #
    #     # Assert
    #     mock_spotify_get_related_artists.assert_called_once_with(
    #         artist_id=self.artist_id
    #     )
    #     mock_get_artists_ids.assert_called_once()
    #
    #     # Check if insert_artist is called for the new related artists
    #     self.assertEqual(mock_insert_artist.call_count, 2)
    #     self.assertEqual(mock_insert_related_artist_user.call_count, 2)
    #
    #     expected_calls = [
    #         ({"artist": Artist.model_validate(self.related_artists[0])},),
    #         ({"artist": Artist.model_validate(self.related_artists[1])},),
    #     ]
    #     mock_insert_artist.assert_has_calls(expected_calls, any_order=True)
    #
    #     expected_related_artist_calls = [
    #         ({"related_artist_id": "related_artist_1", "artist_id": self.artist_id},),
    #         ({"related_artist_id": "related_artist_2", "artist_id": self.artist_id},),
    #     ]
    #     mock_insert_related_artist_user.assert_has_calls(
    #         expected_related_artist_calls, any_order=True
    #     )


if __name__ == "__main__":
    unittest.main()
