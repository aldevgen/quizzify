import logging

from quizzify.crud import albums as crud_albums
from quizzify.crud import artists as crud_artists
from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import SongQuestionType
from quizzify.spotify.spotify_requests import (
    spotify_get_album,
    spotify_get_artist_albums_ids,
)
from quizzify.utils.schemas import Album

logger = logging.getLogger(__name__)


class QuestionSongAlbum(AbstractQuestion):
    """Song question class."""

    def __init__(
        self,
        artist_id,
        artist_name,
        album_id,
        album_name,
        song_id,
        song_name,
        answer,
    ) -> None:
        """Song question constructor."""
        super().__init__()
        self.incorrect_answers = []
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.album_id = album_id
        self.album_name = album_name
        self.song_id = song_id
        self.song_name = song_name
        self.correct_answer = answer
        self.question_type = SongQuestionType.SONG_ALBUM

    def display_question(self) -> str:
        """Display the question about the song's album.

        Returns
        -------
        str
            The string corresponding to the question about the song's album.
        """
        return f"In which album is the song '{self.song_name}' from {self.artist_name}?"

    def set_incorrect_answers(self):
        """Set incorrect answers for any song album question.

        This method fetches the artist's albums from the database and Spotify API.
        If the artist has more than 3 albums in the database, it randomly selects 3.
        Otherwise, it fetches data from the Spotify API. If the artist has less
        than 3 albums, it fetches related artists' albums.

        Steps:
        1. Fetch the artist's albums from the database.
        2. If the artist has more than 3 albums, select 3 random albums.
        3. If the artist has 3 or fewer albums in the database, fetch additional albums
           from the Spotify API.
        4. If necessary, fetch related artists' albums to reach the required number of
           incorrect answers.

        Notes
        -----
        The method updates the `incorrect_answers` attribute with incorrect album names.
        """
        artists_albums = crud_albums.get_artists_albums(self.artist_id)
        nb_albums = len(artists_albums)
        logger.info(f"Artist {self.artist_name} has {nb_albums} albums in DB.")
        if artists_albums:
            if nb_albums > 3:
                # retrieve at least 3 incorrect albums
                logger.info(f"Fetching {self.artist_name}'s albums from DB.")
                albums = crud_albums.get_random_album_name_by_artist_id_exclude_album(
                    artist_id=self.artist_id,
                    exclude_album_id=self.album_id,
                    limit=3,
                )
                self.incorrect_answers = albums
            else:
                # fetch artist's albums from Spotify
                logger.info(f"Fetching {self.artist_name}'s albums from Spotify API.")
                artist_albums_ids = spotify_get_artist_albums_ids(
                    artist_id=self.artist_id,
                )
                nb_spotify_artist_albums = len(artist_albums_ids)
                logger.info(
                    f"Artist {self.artist_name} has {nb_spotify_artist_albums} "
                    f"albums (Spotify API)."
                )
                albums_ids = crud_albums.get_artists_albums_ids(
                    artist_id=self.artist_id,
                )
                # insert new albums in the DB
                for album_id in artist_albums_ids:
                    if album_id not in albums_ids:
                        albums_ids.append(album_id)
                        album_info = spotify_get_album(
                            album_id=album_id,
                        )
                        crud_albums.insert_album(
                            album=Album.model_validate(album_info),
                            artist_id=self.artist_id,
                        )

                # artist's albums in the database
                albums_name = (
                    crud_albums.get_random_album_name_by_artist_id_exclude_album(
                        artist_id=self.artist_id,
                        exclude_album_id=self.album_id,
                        limit=3,
                    )
                )
                if nb_spotify_artist_albums > 3:
                    # return random albums from the DB
                    self.incorrect_answers = albums_name

                else:
                    # if artist has less than 3 albums fetch related artists albums
                    nb_albums_to_fetch = 3 - nb_spotify_artist_albums + 1
                    related_artist_ids = crud_artists.get_random_related_artist_ids(
                        artist_id=self.artist_id,
                        nb_artists=nb_albums_to_fetch,
                    )
                    related_albums_name = []
                    for related_artist_id in related_artist_ids:
                        related_artist_albums = crud_albums.get_artists_albums(
                            artist_id=related_artist_id,
                        )
                        if related_artist_albums:
                            related_album = (
                                crud_albums.get_random_album_name_by_artist_id(
                                    artist_id=related_artist_id,
                                    limit=1,
                                )[0]
                            )
                            related_albums_name.append(related_album)
                        else:
                            # if no related albums, fetch random albums from Spotify API
                            related_artist_albums_ids = (
                                crud_albums.get_artists_albums_ids(
                                    artist_id=related_artist_id,
                                )
                            )
                            spotify_related_artist_albums_ids = (
                                spotify_get_artist_albums_ids(
                                    artist_id=related_artist_id,
                                )
                            )
                            for album_id in spotify_related_artist_albums_ids:
                                if album_id not in related_artist_albums_ids:
                                    related_artist_albums_ids.append(album_id)
                                    album_info = spotify_get_album(
                                        album_id=album_id,
                                    )
                                    crud_albums.insert_album(
                                        album=Album.model_validate(album_info),
                                        artist_id=related_artist_id,
                                    )
                            related_random_album_name = (
                                crud_albums.get_random_album_name_by_artist_id(
                                    artist_id=related_artist_id,
                                    limit=1,
                                )
                            )[0]
                            related_albums_name.append(related_random_album_name)
                        self.incorrect_answers = albums_name + related_albums_name
