import unittest

from quizzify.crud import albums as crud_albums
from quizzify.utils.schemas import Album


class TestCrudAlbums(unittest.TestCase):
    def test_get_albums_ids(self):
        # Given
        expected_result = [
            "2coqGqbnSCAy740mClWesA",
            "0sNOF9WDwhWunNAHPD3Baj",
            "2ZUwFxlDV6dP8y2fMs59fN",
        ]

        # When
        result = crud_albums.get_albums_ids()

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 3)

    def test_get_random_album(self):
        # Given
        user_id = "abc123def456"
        expected_result = [
            "I Don't Speak The Language",
            "Il ballo della vita",
            "Hybrid Theory",
        ]

        # When
        result = crud_albums.get_random_album(user_id=user_id)

        # Then
        self.assertIn(result["album_name"], expected_result)

    def test_insert_album(self):
        # Given
        expected_result = [
            "2coqGqbnSCAy740mClWesA",
            "0sNOF9WDwhWunNAHPD3Baj",
            "2ZUwFxlDV6dP8y2fMs59fN",
            "44a7Wk3Jh2JGVhjcFYWozj",
        ]
        album = Album(
            id="44a7Wk3Jh2JGVhjcFYWozj",
            name="Il ballo della vita",
            popularity=69,
            release_year="2018",
            total_tracks=12,
            image_url="https://i.scdn.co/image/fake_image",
        )
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"

        # When
        crud_albums.insert_album(album, artist_id)

        # Then - check if the album was inserted
        result = crud_albums.get_albums_ids()

        self.assertIn(album.id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 4)
