import unittest

from quizzify.crud import songs as crud_songs
from quizzify.utils.schemas import Song


class TestCrudSong(unittest.TestCase):
    def test_get_songs_ids(self):
        # Given
        expected_result = [
            "1mCsF9Tw4AkIZOjvZbZZdT",
            "6hQ5vU4jWvz1bXjXj3t7yT",
            "2gMXnyrvIjhVBUZwvLZDMP",
        ]

        # When
        result = crud_songs.get_songs_ids()

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 3)

    def test_get_random_song(self):
        # Given
        user_id = "abc123def456"
        expected_song_name = [
            "Break My Stride",
            "Beggin'",
            "In the End",
        ]
        expected_album_name = [
            "I Don't Speak The Language",
            "Il ballo della vita",
            "Hybrid Theory",
        ]
        expected_artist_name = [
            "Matthew Wilder",
            "Måneskin",
            "Linkin Park",
        ]
        # When
        result = crud_songs.get_random_song(user_id=user_id)

        # Then
        self.assertIn(member=result["song_name"], container=expected_song_name)
        self.assertIn(member=result["album_name"], container=expected_album_name)
        self.assertIn(member=result["artist_name"], container=expected_artist_name)

    def test_insert_song(self):
        # Given
        expected_result = [
            "1mCsF9Tw4AkIZOjvZbZZdT",
            "6hQ5vU4jWvz1bXjXj3t7yT",
            "2gMXnyrvIjhVBUZwvLZDMP",
            "3590AAEoqH50z4UmhMIY85",
        ]

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
        self.assertEqual(len(result), 4)
