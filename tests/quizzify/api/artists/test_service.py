import unittest
from unittest.mock import patch

from quizzify.api.artists import service
from quizzify.utils.schemas import TimeRange


# write tests for the artist service functions with the mocks for the database functions
class TestArtistService(unittest.TestCase):
    @patch("quizzify.api.artists.service.get_top_artists")
    def test_get_top_artists(self, mock_get_top_artists):
        # mock the return value of the database function
        mock_get_top_artists.return_value = {
            "id": "artist_id",
            "name": "artist_name",
            "popularity": 80,
            "genres": ["pop", "rock"],
            "followers": 1000,
            "image_url": "https://fake_image_url.com",
        }

        # call the function to test
        top_artists = service.get_top_artists(
            time_range=TimeRange.SHORT_TERM,
            limit=1,
        )

        # check the return value
        self.assertEqual(
            top_artists,
            {
                "id": "artist_id",
                "name": "artist_name",
                "popularity": 80,
                "genres": ["pop", "rock"],
                "followers": 1000,
                "image_url": "https://fake_image_url.com",
            },
        )

        # check if the database function was called
        mock_get_top_artists.assert_called_once_with(
            time_range=TimeRange.SHORT_TERM,
            limit=1,
        )

    @patch("quizzify.api.artists.service.crud.get_random_artist")
    def test_get_random_artist(self, mock_get_random_artist):
        # mock the return value of the database function
        mock_get_random_artist.return_value = {
            "id": "artist_id_1",
            "name": "artist_name_1",
            "popularity": 80,
            "genres": ["pop", "rock"],
            "followers": 1000,
            "image_url": "https://image_url_1.com",
        }

        # call the function to test
        random_artist = service.get_random_artist()

        # check the return value
        self.assertEqual(
            random_artist,
            {
                "id": "artist_id_1",
                "name": "artist_name_1",
                "popularity": 80,
                "genres": ["pop", "rock"],
                "followers": 1000,
                "image_url": "https://image_url_1.com",
            },
        )

        # check if the database function was called
        mock_get_random_artist.assert_called_once()
