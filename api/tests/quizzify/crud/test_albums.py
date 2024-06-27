import unittest

from quizzify.crud import albums as crud_albums
from quizzify.utils.schemas import Album


class TestCrudAlbums(unittest.TestCase):
    def test_get_albums_ids(self):
        expected_result = [
            "2kcJ3TxBhSwmki0QWFXUz8",
            "3wLMnrlPtVSADxalu9kIxK",
            "7KF1Ain9mYYlg5M46g0i4A",
            "44a7Wk3Jh2JGVhjcFYWozj",
            "2qJw6w5XwQO0PQlSWPu7Tw",
        ]
        # Given

        # When
        result = crud_albums.get_albums_ids()

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 5)

    def test_get_artists_albums_ids(self):
        # Given
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"
        expected_result = [
            "2kcJ3TxBhSwmki0QWFXUz8",
            "3wLMnrlPtVSADxalu9kIxK",
            "7KF1Ain9mYYlg5M46g0i4A",
            "44a7Wk3Jh2JGVhjcFYWozj",
            "2qJw6w5XwQO0PQlSWPu7Tw",
        ]

        # When
        result = crud_albums.get_artists_albums_ids(artist_id=artist_id)

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 5)

    def test_get_artists_albums(self):
        # Given
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"
        expected_result = [
            "2kcJ3TxBhSwmki0QWFXUz8",
            "3wLMnrlPtVSADxalu9kIxK",
            "7KF1Ain9mYYlg5M46g0i4A",
            "44a7Wk3Jh2JGVhjcFYWozj",
            "2qJw6w5XwQO0PQlSWPu7Tw",
        ]

        # When
        result = crud_albums.get_artists_albums(artist_id=artist_id)

        # Then
        self.assertIn(result[0]["album_id"], expected_result)
        self.assertIn(result[1]["album_id"], expected_result)
        self.assertIn(result[2]["album_id"], expected_result)
        self.assertIn(result[3]["album_id"], expected_result)
        self.assertIn(result[4]["album_id"], expected_result)
        self.assertEqual(len(result), 5)

    def test_get_random_album(self):
        # Given
        user_id = "abc123def456"
        expected_result = {
            "artist_id": "0lAWpj5szCSwM4rUMHYmrr",
            "artist_name": "Måneskin",
            "album_id": "44a7Wk3Jh2JGVhjcFYWozj",
            "album_name": "Il ballo della vita",
            "popularity": 70,
            "release_year": "2018",
            "release_decade": "2010",
            "total_tracks": 12,
            "image_url": "https://i.scdn.co/image/"
            "ab67616d0000b273dbc892b8194e35ca3524e767",
        }

        # When
        result = crud_albums.get_random_album(user_id=user_id)

        # Then
        self.assertEqual(result["artist_id"], expected_result["artist_id"])
        self.assertEqual(result["artist_name"], expected_result["artist_name"])
        self.assertEqual(result["album_id"], expected_result["album_id"])
        self.assertEqual(result["album_name"], expected_result["album_name"])
        self.assertEqual(result["popularity"], expected_result["popularity"])
        self.assertEqual(result["release_year"], expected_result["release_year"])
        self.assertEqual(result["release_decade"], expected_result["release_decade"])
        self.assertEqual(result["total_tracks"], expected_result["total_tracks"])
        self.assertEqual(result["image_url"], expected_result["image_url"])

    def test_insert_album(self):
        # Given
        expected_result = [
            "2kcJ3TxBhSwmki0QWFXUz8",
            "3wLMnrlPtVSADxalu9kIxK",
            "7KF1Ain9mYYlg5M46g0i4A",
            "44a7Wk3Jh2JGVhjcFYWozj",
            "2qJw6w5XwQO0PQlSWPu7Tw",
            "1uROBP2G4MP0O4w1v5Cpbg",
        ]
        album = Album(
            id="1uROBP2G4MP0O4w1v5Cpbg",
            name="Imploding The Mirage",
            popularity=56,
            release_year="2020",
            release_decade="2020",
            total_tracks=10,
            image_url="https://i.scdn.co/image/"
            "ab67616d0000b273f08d82ff69ae975e6e5f395e",
        )

        # When
        crud_albums.insert_album(album)

        # Then - check if the album was inserted
        result = crud_albums.get_albums_ids()

        self.assertIn(album.id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 6)
