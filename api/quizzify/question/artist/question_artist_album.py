from quizzify.crud import albums as crud_albums
from quizzify.crud import artists as crud_artists
from quizzify.question.abstract_question import AbstractQuestion
from quizzify.question.question_types import ArtistQuestionType


class QuestionArtistAlbum(AbstractQuestion):
    """Artist question class."""

    def __init__(self, artist_id, artist_name, album_name, answer) -> None:
        """Artist question constructor."""
        super().__init__()
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
        and then gets a random album from these artists.
        """
        artist_ids = crud_artists.get_random_related_artist(self.artist_id)
        album_names = [
            crud_albums.get_random_album_by_artist_id(
                artist_id=artist_id["related_artist_id"]
            )["album_name"]
            for artist_id in artist_ids
        ]
        self.incorrect_answers = album_names
