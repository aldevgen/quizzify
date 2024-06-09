import unittest

from quizzify.crud import artists as crud_artists
from quizzify.utils.schemas import Artist


class TestCrudArtists(unittest.TestCase):
    def test_get_artists_ids(self):
        # Given
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "6XyY86QOPPrYVGvF9ch6wz",
            "3bmFPbLMiLxtR9tFrTcKcP",
        ]

        # When
        result = crud_artists.get_artists_ids()

        # Then
        self.assertIn(result[0], expected_result)
        self.assertIn(result[1], expected_result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 3)

    def test_get_random_artist(self):
        # Given
        expected_result = ["Måneskin", "Linkin Park", "Matthew Wilder"]

        # When
        result = crud_artists.get_random_artist()

        # Then
        self.assertIn(result[0]["name"], expected_result)

    def test_insert_artist(self):
        # Given
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "6XyY86QOPPrYVGvF9ch6wz",
            "3bmFPbLMiLxtR9tFrTcKcP",
            "0C0XlULifJtAgn6ZNCW2eu",
        ]
        artist = Artist(
            id="0C0XlULifJtAgn6ZNCW2eu",
            name="The Killers",
            popularity=75,
            genres=[
                "alternative rock",
                "dance rock",
                "modern rock",
                "permanent wave",
                "rock",
            ],
            followers=7281678,
            image_url="https://i.scdn.co/image/fake_image",
        )

        # When
        crud_artists.insert_artist(artist)

        # Then - check if the artist was inserted
        result = crud_artists.get_artists_ids()

        self.assertIn(artist.id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 4)
