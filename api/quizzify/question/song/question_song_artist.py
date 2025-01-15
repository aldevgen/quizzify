import logging
import random

from quizzify.api.lastfm.lastfm_requests import lastfm_get_similar_artists
from quizzify.api.spotify.spotify_requests import spotify_get_artist_info_from_name
from quizzify.crud import artists as crud_artists
from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import SongQuestionType
from quizzify.utils.schemas import Artist

logger = logging.getLogger(__name__)


class QuestionSongArtist(AbstractQuestion):
    """Song question class."""

    def __init__(
        self,
        artist_id,
        artist_name,
        song_id,
        song_name,
        answer,
    ) -> None:
        """Song question constructor."""
        super().__init__()
        self.incorrect_answers = []
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.song_id = song_id
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = SongQuestionType.SONG_ARTIST

    def display_question(self) -> str:
        """Get a song question."""
        return f"Which artist sings '{self.song_name}'?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the song question."""
        related_artists = crud_artists.get_random_related_artist_ids(
            artist_id=self.artist_id,
            nb_artists=3,
        )
        if related_artists:
            logger.info(f"Fetching {self.artist_name}'s related artists from DB.")
            related_artist_names = [
                crud_artists.get_artist_name(artist_id=artist_id)
                for artist_id in related_artists
            ]
            self.incorrect_answers = related_artist_names
        else:
            logger.info(
                f"No related artists found in the database, "
                f"fetching {self.artist_name}'s related artists from Spotify API."
            )
            # fetch related artists from Spotify
            related_artists = lastfm_get_similar_artists(
                artist_name=self.artist_name,
            )

            artists_ids = crud_artists.get_artists_ids()
            # insert data in the database if not present
            for related_artist in related_artists:
                # check if related artist is already in the database
                related_artist_info = spotify_get_artist_info_from_name(
                    artist_name=related_artist,
                )
                related_artist_id = related_artist_info["id"]
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
