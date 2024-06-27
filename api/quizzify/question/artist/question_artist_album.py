import logging

from quizzify.crud import albums as crud_albums
from quizzify.crud import artists as crud_artists
from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import ArtistQuestionType
from quizzify.spotify.spotify_requests import (
    spotify_get_album,
    spotify_get_artist_albums_ids,
    spotify_get_related_artists,
)
from quizzify.utils.schemas import Album, Artist

logger = logging.getLogger(__name__)


class QuestionArtistAlbum(AbstractQuestion):
    """Artist question class."""

    def __init__(self, artist_id, artist_name, album_name, answer) -> None:
        """Artist question constructor."""
        super().__init__()
        self.incorrect_answers = []
        self.question_type = ArtistQuestionType.ARTIST_ALBUM
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.album_name = album_name
        self.correct_answer = answer

    def display_question(self) -> str:
        """Get an artist question."""
        return f"Which album is from the artist {self.artist_name}?"

    def set_incorrect_answers(self):
        """Set incorrect answers for the artist album question.

        This method gets a list of random artists related to the current artist
        and then gets one random album from these artists.
        """
        related_artist_ids = crud_artists.get_random_related_artist_ids(
            artist_id=self.artist_id,
            nb_artists=3,
        )
        # related artists found in the database
        if related_artist_ids:
            for related_artist_id in related_artist_ids:
                album_name = crud_albums.get_random_album_name_by_artist_id(
                    artist_id=related_artist_id,
                    limit=1,
                )
                # if artist has an album then append it to the incorrect answers
                if album_name:
                    self.incorrect_answers.append(album_name)
                else:
                    logger.info(
                        f"Related artist ID {related_artist_id} has no albums, "
                        f"fetching albums from Spotify API."
                    )
                    artist_albums_ids = spotify_get_artist_albums_ids(
                        artist_id=related_artist_id,
                    )
                    albums_ids = crud_albums.get_albums_ids()
                    # insert new albums in the DB
                    for album_id in artist_albums_ids:
                        if album_id not in albums_ids:
                            albums_ids.append(album_id)
                            # get album info from Spotify API
                            album_info = spotify_get_album(
                                album_id=album_id,
                            )
                            # insert album in the DB
                            crud_albums.insert_album(
                                album=Album.model_validate(album_info),
                            )
                            # insert relation between album and artist in the DB
                            crud_albums.insert_album_artist(
                                album_id=album_id,
                                artist_id=related_artist_id,
                            )
                    # fetch one random album from the related artist in the DB
                    album_name = crud_albums.get_random_album_name_by_artist_id(
                        artist_id=related_artist_id,
                        limit=1,
                    )
                    self.incorrect_answers.append(album_name)
        else:
            # fetching related artists from Spotify API
            logger.info(
                f"No related artists found in the database, "
                f"fetching {self.artist_name}'s related artists from Spotify API."
            )
            # fetch related artists from Spotify
            related_artists = spotify_get_related_artists(
                artist_id=self.artist_id,
            )
            # get artists IDs from the database
            artists_ids = crud_artists.get_artists_ids()
            # get albums IDs from the database
            albums_ids = crud_albums.get_albums_ids()

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
                        artist_id=self.artist_id,
                        related_artist_id=related_artist_id,
                    )
                    # fetch artist's albums from Spotify
                    artist_albums_ids = spotify_get_artist_albums_ids(
                        artist_id=related_artist_id,
                    )
                    for album_id in artist_albums_ids:
                        if album_id not in albums_ids:
                            album_info = spotify_get_album(
                                album_id=album_id,
                            )
                            crud_albums.insert_album(
                                album=Album.model_validate(album_info),
                            )
                            crud_albums.insert_album_artist(
                                album_id=album_id,
                                artist_id=related_artist_id,
                            )
                            albums_ids.append(album_id)

            # fetch random related artists from the database
            related_artist_ids = crud_artists.get_random_related_artist_ids(
                artist_id=self.artist_id,
                nb_artists=3,
            )
            for related_artist_id in related_artist_ids:
                album_name = crud_albums.get_random_album_name_by_artist_id(
                    artist_id=related_artist_id,
                    limit=1,
                )
                self.incorrect_answers.append(album_name)
