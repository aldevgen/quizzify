import unittest

from quizzify.crud import artists as crud_artists
from quizzify.utils.schemas import Artist


class TestCrudArtists(unittest.TestCase):
    def test_get_artists_ids(self):
        # Given
        expected_result = [
            "0lAWpj5szCSwM4rUMHYmrr",
            "0C0XlULifJtAgn6ZNCW2eu",
        ]

        # When
        result = crud_artists.get_artists_ids()

        # Then
        self.assertIn(result[0], expected_result)
        self.assertIn(result[1], expected_result)
        self.assertEqual(result, expected_result)
        self.assertEqual(len(result), 2)

    def test_get_random_artist(self):
        # Given
        user_id = "abc123def456"
        expected_result = {
            "artist_id": "0lAWpj5szCSwM4rUMHYmrr",
            "artist_name": "Måneskin",
            "popularity": 79,
            "genres": ["indie rock italiano", "italian pop"],
            "image_url": "https://i.scdn.co/image/"
            "ab6761610000e5eb46d0db8a86fda630ec12401f",
        }

        # When
        result = crud_artists.get_random_artist(user_id=user_id)

        # Then
        self.assertEqual(result["id"], expected_result["artist_id"])
        self.assertEqual(result["name"], expected_result["artist_name"])
        self.assertEqual(result["popularity"], expected_result["popularity"])
        self.assertEqual(result["genres"], expected_result["genres"])
        self.assertEqual(result["image_url"], expected_result["image_url"])


#
#     def test_insert_artist(self):
#         # Given
#         expected_result = [
#             "0lAWpj5szCSwM4rUMHYmrr",
#             "6XyY86QOPPrYVGvF9ch6wz",
#             "3bmFPbLMiLxtR9tFrTcKcP",
#             "0C0XlULifJtAgn6ZNCW2eu",
#         ]
#         artist = Artist(
#             id="0C0XlULifJtAgn6ZNCW2eu",
#             name="The Killers",
#             popularity=75,
#             genres=[
#                 "alternative rock",
#                 "dance rock",
#                 "modern rock",
#                 "permanent wave",
#                 "rock",
#             ],
#             followers=7281678,
#             image_url="https://i.scdn.co/image/fake_image",
#         )
#
#         # When
#         crud_artists.insert_artist(artist)
#
#         # Then - check if the artist was inserted
#         result = crud_artists.get_artists_ids()
#
#         self.assertIn(artist.id, result)
#         self.assertEqual(result, expected_result)
#         self.assertEqual(len(result), 4)
