import doctest


class Song:
    """ Song class with title, artist, length in seconds
    """

    def __init__(self, title: str, artist: str, length: int) -> None:
        """ initialize an instance of Song with given title, artist and length
        >>> my_song = Song('Martin & Gina', 'Polo G', 160)
        """
        self.__title = title
        self.__artist = artist
        self.__length = length


    def __str__(self) -> str:
        """returns a human readable string with attributes from Song object
        >>> s = Song('Jump', 'van Halen', 234)
        >>> str(s)
        'Jump by van Halen, 234 seconds long'
        """
        return f'{self.__title} by {self.__artist}, {self.__length} seconds long'


    def __repr__(self) -> str:
        """returns a string that matches the creation of that Song object
        >>> s = Song('Jump', 'van Halen', 234)
        >>> repr(s)
        "Song('Jump', 'van Halen', 234)"
        """
        return (f'Song({repr(self.__title)}, {repr(self.__artist)}, '
                   + f'{repr(self.__length)})')


    def __eq__(self, other: 'Song') -> bool:
        """ returns True if same song, False otherwise
        >>> s1 = Song('Jump', 'van Halen', 234)
        >>> s2 = Song('Jump', 'van Halen', 255)
        >>> s3 = Song('Jump', 'Pointer Sisters', 234)
        >>> s1==s1
        True
        >>> s1==s2
        True
        >>> s1==s3
        False
        """
        return (self.__title == other.__title
                and self.__artist == other.__artist)

    def get_title(self) -> str:
        """ returns title of Song self
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.get_title()
        'Despacito'
        """
        return self.__title

    def set_title(self, title: str) -> None:
        """ sets artist of Song self to given artist
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.set_title('Boyfriend')
        >>> sng
        Song('Boyfriend', 'Justin Bieber', 225)
        """
        self.__title = title

    def get_artist(self) -> str:
        """ returns title of Song self
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.get_artist()
        'Justin Bieber'
        """
        return self.__artist

    def set_artist(self, artist: str) -> None:
        """ sets artist of Song self to given artist
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.set_artist('J. Bieber')
        >>> sng
        Song('Despacito', 'J. Bieber', 225)
        """
        self.__artist = artist

    def get_length(self) -> int:
        """ returns length of Song self
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.get_length()
        225
        """
        return self.__length

    def set_length(self, length: int) -> None:
        """ sets length of Song self to given length
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.set_length(260)
        >>> sng
        Song('Despacito', 'Justin Bieber', 260)
        """
        self.__length = length

    def add_time(self, time: int) -> None:
        """ adds time to the length of Song self
        Precondition: time>=0
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.add_time(25)
        >>> sng
        Song('Despacito', 'Justin Bieber', 250)
        """
        self.__length += time

    def is_written_by(self, artist: str) -> bool:
        """ returns True if artist of Song self matches given artist
        ignoring case, False otherwise
        >>> sng = Song('Despacito', 'Justin Bieber', 225)
        >>> sng.is_written_by('Justin Bieber')
        True
        >>> sng.is_written_by('justin BIEBER')
        True
        >>> sng.is_written_by('Justin Trudeau')
        False
        """
        return self.__artist.lower() == artist.lower()
