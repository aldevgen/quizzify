import unittest

from quizzify.crud import artists as crud_artists
from quizzify.utils.schemas import Artist


class TestCrudArtists(unittest.TestCase):
    def test_get_artists_ids(self):
        # Given
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "0C0XlULifJtAgn6ZNCW2eu",
            "7Ln80lUS6He07XvHI8qqHH",
        ]

        # When
        result = crud_artists.get_artists_ids()

        # Then
        self.assertIn(result[0], expected_result)
        self.assertIn(result[1], expected_result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 3)

    def test_get_top_artists(self):
        # Given
        user_id = "abc123def456"
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "0C0XlULifJtAgn6ZNCW2eu",
        ]

        # When
        result = crud_artists.get_top_artists(user_id=user_id)

        # Then
        self.assertIn(result[0]["id"], expected_result)
        self.assertEqual(len(result), 1)

    def test_get_random_artist(self):
        # Given
        user_id = "abc123def456"
        expected_result = {
            "artist_id": "0lAWpj5szCSwM4rUMHYmrr",
            "artist_name": "Måneskin",
            "popularity": 79,
            "genres": ["indie rock italiano", "italian pop"],
            "image_url": (
                "https://i.scdn.co/image/ab6761610000e5eb46d0db8a86fda630ec12401f"
            ),
        }

        # When
        result = crud_artists.get_random_artist(user_id=user_id)

        # Then
        self.assertEqual(result["id"], expected_result["artist_id"])
        self.assertEqual(result["name"], expected_result["artist_name"])
        self.assertEqual(result["popularity"], expected_result["popularity"])
        self.assertEqual(result["genres"], expected_result["genres"])
        self.assertEqual(result["image_url"], expected_result["image_url"])

    def test_get_artist_name(self):
        # Given
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"
        expected_result = "Måneskin"

        # When
        result = crud_artists.get_artist_name(artist_id=artist_id)

        # Then
        self.assertEqual(result, expected_result)

    def test_get_random_artist_album(self):
        # Given
        user_id = "abc123def456"
        expected_artist_ids = [
            "0lAWpj5szCSwM4rUMHYmrr",
        ]
        expected_artist_names = [
            "Måneskin",
        ]
        expected_albums_ids = [
            "2kcJ3TxBhSwmki0QWFXUz8",
            "7KF1Ain9mYYlg5M46g0i4A",
            "3wLMnrlPtVSADxalu9kIxK",
            "2qJw6w5XwQO0PQlSWPu7Tw",
            "44a7Wk3Jh2JGVhjcFYWozj",
        ]
        expected_albums_names = [
            "Teatro d'ira - Vol. I",
            "Chosen",
            "Il ballo della vita",
            "RUSH!",
            "RUSH! (ARE U COMING?)",
        ]

        # When
        result = crud_artists.get_random_artist_album(user_id=user_id)

        # Then
        self.assertIn(result["artist_id"], expected_artist_ids)
        self.assertIn(result["artist_name"], expected_artist_names)
        self.assertIn(result["album_id"], expected_albums_ids)
        self.assertIn(result["album_name"], expected_albums_names)

    def test_get_random_related_artists(self):
        # Given
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"
        expected_result_id = [
            "7Ln80lUS6He07XvHI8qqHH",
        ]

        # When
        result = crud_artists.get_random_related_artists(artist_id=artist_id)

        # Then
        self.assertIn(result[0]["related_artist_id"], expected_result_id)
        self.assertEqual(len(result), 1)

    def test_get_random_related_artist_ids(self):
        # Given
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"
        expected_result = [
            "7Ln80lUS6He07XvHI8qqHH",
        ]

        # When
        result = crud_artists.get_random_related_artist_ids(artist_id=artist_id)

        # Then
        self.assertIn(result[0], expected_result)
        self.assertEqual(len(result), 1)

    def test_get_random_related_artists_name(self):
        # Given
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"
        expected_result = [
            "Arctic Monkeys",
        ]

        # When
        result = crud_artists.get_random_related_artists_name(artist_id=artist_id)

        # Then
        self.assertIn(result[0], expected_result)
        self.assertEqual(len(result), 1)

    def test_insert_artist(self):
        # Given
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "0C0XlULifJtAgn6ZNCW2eu",
            "7Ln80lUS6He07XvHI8qqHH",
            "08GQAI4eElDnROBrJRGE0X",
        ]
        artist = Artist(
            id="08GQAI4eElDnROBrJRGE0X",
            name="Fleetwood Mac",
            popularity=80,
            genres=[
                "album rock",
                "classic rock",
                "rock",
                "soft rock",
                "yacht rock",
            ],
            followers=11571906,
            image_url=(
                "https://i.scdn.co/image/ab6761610000e5ebc8752dd511cda8c31e9daee8"
            ),
        )

        # When
        crud_artists.insert_artist(artist)

        # Then - check if the artist was inserted
        result = crud_artists.get_artists_ids()

        self.assertIn(artist.id, result)
        self.assertCountEqual(result, expected_result)
        self.assertEqual(len(result), 4)

    def test_insert_top_artist_user(self):
        # Given
        artist_id = "0C0XlULifJtAgn6ZNCW2eu"
        user_id = "abc123def456"

        # Before the insert, check if the artist is not in the top artists
        result = crud_artists.get_top_artists_ids(user_id=user_id)
        expected_result = ["0lAWpj5szCSwM4rUMHYmrr"]
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 1)

        # When - insert a new artist as top artist for the user
        crud_artists.insert_top_artist_user(
            artist_id=artist_id,
            user_id=user_id,
            time_range="short_term",
        )

        # Then - check if the artist was inserted
        result = crud_artists.get_top_artists_ids(user_id=user_id)
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "0C0XlULifJtAgn6ZNCW2eu",
        ]
        self.assertIn(artist_id, result)
        self.assertCountEqual(result, expected_result)
        self.assertEqual(len(result), 2)

    def test_insert_related_artist_user(self):
        # Given
        artist_id = "0C0XlULifJtAgn6ZNCW2eu"
        related_artist_id = "7Ln80lUS6He07XvHI8qqHH"

        # Before the insert, check if the artist is not in the related artists
        result = crud_artists.get_related_artists_ids(artist_id=artist_id)
        expected_result = []
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 0)

        # When - insert a new artist as related artist for the user
        crud_artists.insert_related_artist_user(
            artist_id=artist_id,
            related_artist_id=related_artist_id,
        )

        # Then - check if the artist was inserted
        result = crud_artists.get_related_artists_ids(artist_id=artist_id)
        expected_result = [
            "7Ln80lUS6He07XvHI8qqHH",
        ]

        self.assertIn(related_artist_id, result)
        self.assertCountEqual(result, expected_result)
