import random

from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import AlbumQuestionType
from quizzify.spotify.spotify_requests import spotify_get_related_artists


class QuestionAlbumArtist(AbstractQuestion):
    """Album question class."""

    def __init__(
        self,
        album_id,
        album_name,
        artist_id,
        artist_name,
        song_id,
        song_name,
        answer,
    ) -> None:
        """Album question constructor."""
        super().__init__()
        self.album_id = album_id
        self.album_name = album_name
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_id = song_id
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = AlbumQuestionType.ALBUM_ARTIST

    def display_question(self):
        """Get an album question."""
        return f"Which artist wrote the {self.album_name} album?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the album artist question.

        This method uses the Spotify API to get related artists to the artist of the
        album. Then it randomly selects 3 of these artists to be the incorrect answers.
        """
        related_artists = spotify_get_related_artists(artist_id=self.artist_id)
        related_artist_names = [artist["name"] for artist in related_artists]
        self.incorrect_answers = random.sample(related_artist_names, k=3)
