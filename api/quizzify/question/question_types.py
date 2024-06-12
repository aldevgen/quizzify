from enum import Enum


class ExtendedEnum(Enum):
    """Extend the Enum class to provide a method to get all the values of the Enum."""

    @classmethod
    def get_items(cls):
        """Get all the values of the Enum."""
        return list(map(lambda c: c.value, cls))


class QuestionType(ExtendedEnum):
    """Question type class."""

    SONG = "song"
    ALBUM = "album"
    ARTIST = "artist"


class SongQuestionType(ExtendedEnum):
    """Song question type class."""

    SONG_ARTIST = "song_artist"
    SONG_ALBUM = "song_album"


class AlbumQuestionType(ExtendedEnum):
    """Album question type class."""

    ALBUM_ARTIST = "album_artist"
    ALBUM_DECADE = "album_decade"
    # ALBUM_GENRE = "album_genre"
    ALBUM_YEAR = "album_year"


class ArtistQuestionType(ExtendedEnum):
    """Artist question type class."""

    # ARTIST_GENRE = "artist_genre"
    ARTIST_ALBUM = "artist_album"
