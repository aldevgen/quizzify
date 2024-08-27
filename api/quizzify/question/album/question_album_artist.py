import logging
import random

from quizzify.crud import artists as crud_artists
from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import AlbumQuestionType
from quizzify.spotify.spotify_requests import spotify_get_related_artists
from quizzify.utils.schemas import Artist

logger = logging.getLogger(__name__)


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
        self.incorrect_answers = []
        self.album_id = album_id
        self.album_name = album_name
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_id = song_id
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = AlbumQuestionType.ALBUM_ARTIST

    def display_question(self) -> str:
        """Get an album question."""
        return f"Which artist wrote the '{self.album_name}' album?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the album artist question.

        This method uses the Spotify API to get related artists to the artist of the
        album. Then it randomly selects 3 of these artists to be the incorrect answers.
        """
        related_artists = crud_artists.get_random_related_artists_name(
            artist_id=self.artist_id,
            nb_artists=3,
        )
        if related_artists:
            logger.info(
                f"Fetching {self.artist_name}'s related artists from the database."
            )
            self.incorrect_answers = related_artists
        else:
            logger.info(
                f"No related artists found in the database, "
                f"fetching {self.artist_name}'s related artists from Spotify API."
            )
            related_artists = spotify_get_related_artists(artist_id=self.artist_id)
            artists_ids = crud_artists.get_artists_ids()
            # insert data in the database if not present
            for related_artist in related_artists:
                # check if related artist is already in the database
                related_artist_id = related_artist["id"]
                if related_artist_id not in artists_ids:
                    # add related artist to the list of artists in the database
                    artists_ids.append(related_artist_id)
                    crud_artists.insert_artist(
                        artist=Artist.model_validate(related_artist),
                    )
                    # insert artist as top artist for the user
                    crud_artists.insert_related_artist_user(
                        related_artist_id=related_artist_id,
                        artist_id=self.artist_id,
                    )

            related_artists = random.sample(related_artists, k=3)
            related_artist_names = [artist["name"] for artist in related_artists]
            self.incorrect_answers = related_artist_names
