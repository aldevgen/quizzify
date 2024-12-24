import unittest

from quizzify.crud import songs as crud_songs
from quizzify.utils.schemas import Song


class TestCrudSong(unittest.TestCase):
    def test_get_songs_ids(self):
        # Given
        expected_result = [
            "5aWhs651KYM26HYM16kRdk",
        ]

        # When
        result = crud_songs.get_songs_ids()

        # Then
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 1)

    def test_get_top_songs(self):
        # Given
        user_id = "abc123def456"
        expected_result = [
            "5aWhs651KYM26HYM16kRdk",
        ]

        # When
        result = crud_songs.get_top_songs(user_id=user_id)

        # Then
        self.assertIn(result[0]["song_id"], expected_result)
        self.assertEqual(len(result), 1)

    def test_get_random_song(self):
        # Given
        user_id = "abc123def456"
        expected_song = {
            "song_id": "5aWhs651KYM26HYM16kRdk",
            "song_name": "The Man",
            "artist_id": "0C0XlULifJtAgn6ZNCW2eu",
            "artist_name": "The Killers",
            "album_id": "72ZfMxLCPG8mlWC0TXfZQi",
            "album_name": "Wonderful Wonderful",
            "popularity": 63,
            "duration_ms": 250093,
            "track_number": 2,
        }
        # When
        result = crud_songs.get_random_song(user_id=user_id)

        # Then
        self.assertEqual(result["song_id"], expected_song["song_id"])
        self.assertEqual(result["song_name"], expected_song["song_name"])
        self.assertEqual(result["artist_id"], expected_song["artist_id"])
        self.assertEqual(result["artist_name"], expected_song["artist_name"])
        self.assertEqual(result["album_id"], expected_song["album_id"])
        self.assertEqual(result["album_name"], expected_song["album_name"])
        self.assertEqual(result["popularity"], expected_song["popularity"])
        self.assertEqual(result["duration_ms"], expected_song["duration_ms"])
        self.assertEqual(result["track_number"], expected_song["track_number"])

    def test_insert_song(self):
        # Given
        expected_result = [
            "5aWhs651KYM26HYM16kRdk",
            "1vwEgKpkdY63nX0jrrYj9X",
        ]

        song = Song(
            id="1vwEgKpkdY63nX0jrrYj9X",
            name="The Calling",
            artist_id="0C0XlULifJtAgn6ZNCW2eu",
            album_id="72ZfMxLCPG8mlWC0TXfZQi",
            popularity=33,
            duration_ms=241786,
            track_number=9,
        )

        # When
        crud_songs.insert_song(song)

        # Then - check if the song was inserted
        result = crud_songs.get_songs_ids()

        self.assertIn(song.id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 2)

    def test_insert_top_song_user(self):
        # Given
        song_id = "1vwEgKpkdY63nX0jrrYj9X"
        user_id = "abc123def456"

        # Before the insert, check if the song is not in the top songs
        result = crud_songs.get_top_songs_ids(user_id=user_id)
        expected_result = ["5aWhs651KYM26HYM16kRdk"]
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 1)

        # When - insert a new song as top song for the user
        crud_songs.insert_top_song_user(song_id, user_id)

        # Then - check if the song was inserted
        result = crud_songs.get_top_songs_ids(user_id=user_id)
        expected_result = [
            "5aWhs651KYM26HYM16kRdk",
            "1vwEgKpkdY63nX0jrrYj9X",
        ]

        self.assertIn(song_id, result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 2)
