import unittest
from quizzify.crud import songs as crud_songs
from quizzify.utils.schemas import Song


class TestCrudSong(unittest.TestCase):
    def test_get_songs_ids(self):
        # Given
        expected_result = ['1mCsF9Tw4AkIZOjvZbZZdT']

        # When
        result = crud_songs.get_songs_ids()

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 1)

    def test_get_random_song(self):
        # Given
        # When
        result = crud_songs.get_random_song()

        # Then
        self.assertIn(result[0]['song_name'], ['Break My Stride'])
        self.assertIn(result[0]['album_name'], ["I Don't Speak The Language"])
        self.assertIn(result[0]['artist_name'], ['Matthew Wilder'])

    def test_insert_song(self):
        # Given
        expected_result = ['1mCsF9Tw4AkIZOjvZbZZdT', '3590AAEoqH50z4UmhMIY85']

        song = Song(
            id="3590AAEoqH50z4UmhMIY85",
            name="Torna a casa",
            artist_id="0lAWpj5szCSwM4rUMHYmrr",
            album_id="44a7Wk3Jh2JGVhjcFYWozj",
            popularity=80,
            duration_ms=205226,
            track_number=2,
        )

        # When
        crud_songs.insert_song(song)

        # Then - check if the song was inserted
        result = crud_songs.get_songs_ids()

        self.assertIn(song.id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 2)
