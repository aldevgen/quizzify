import unittest
from quizzify.crud import albums as crud_albums
from quizzify.utils.schemas import Album


class TestCrudAlbums(unittest.TestCase):
    def test_get_albums_ids(self):
        # Given
        expected_result = ['2coqGqbnSCAy740mClWesA']

        # When
        result = crud_albums.get_albums_ids()

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 1)

    def test_get_random_album(self):
        # Given
        expected_result = ["I Don't Speak The Language", "Il ballo della vita"]

        # When
        result = crud_albums.get_random_album()

        # Then
        self.assertIn(result[0]['album_name'], expected_result)

    def test_insert_album(self):
        # Given
        expected_result = ['2coqGqbnSCAy740mClWesA', '44a7Wk3Jh2JGVhjcFYWozj']
        album = Album(
            id="44a7Wk3Jh2JGVhjcFYWozj",
            name="Il ballo della vita",
            popularity=69,
            release_year="2018",
            total_tracks=12,
            image_url="https://i.scdn.co/image/ab67616d0000b273f3d4d3f6c3d0c2e8f5c3c4b0",
        )
        artist_id = "0lAWpj5szCSwM4rUMHYmrr"

        # When
        crud_albums.insert_album(album, artist_id)

        # Then - check if the album was inserted
        result = crud_albums.get_albums_ids()

        self.assertIn(album.id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 2)