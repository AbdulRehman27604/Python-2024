import doctest
from song import Song

class Playlist():
    """
    Playlist class that stores a list of songs.
    """
    
    def __init__(self):
        self.songs = []
    
    def __str__(self):
        return str(self.get_songs_as_strings())
    
    def __repr__(self):
        return str(self.songs)
    
    def load_from_file(self, filename: str) -> None:
        """
        Append the songs found within the file to the playlist.
        >>> pl = Playlist()
        >>> pl.load_from_file('playlist.csv')
        >>> pl
        [Song('Lost', 'Frank Ocean', 145), Song('Jump', 'van Halen', 234), Song('Despacito', 'Justin Bieber', 225), Song('Jump', 'Pointer Sisters', 255), Song('Hello', 'Adele', 244), Song('Hello', 'Lionel Richie', 206), Song('Eleanor Rigby', 'Beatles', 128), Song('Yellow Submarine', 'Beatles', 159), Song('Sandstorm', 'Darude', 225), Song('Pokemon Theme', 'Pokemon', 279)]
        """
        file_handle = open(filename, 'r')
        
        for line in file_handle:
            line = line.strip()
            title, artist, length = line.split(',')
            length = int(length)
            
            song = Song(title, artist, length)
            self.songs.append(song)
            
        file_handle.close()
        
    def get_songs(self) -> list[Song]:
        """
        Get the songs in the playlist as a list.
        >>> pl = Playlist()
        >>> pl.load_from_file('playlist.csv')
        >>> pl.get_songs()
        [Song('Lost', 'Frank Ocean', 145), Song('Jump', 'van Halen', 234), Song('Despacito', 'Justin Bieber', 225), Song('Jump', 'Pointer Sisters', 255), Song('Hello', 'Adele', 244), Song('Hello', 'Lionel Richie', 206), Song('Eleanor Rigby', 'Beatles', 128), Song('Yellow Submarine', 'Beatles', 159), Song('Sandstorm', 'Darude', 225), Song('Pokemon Theme', 'Pokemon', 279)]
        """
        return self.songs
    
    def append_song(self, new_song: Song) -> None:
        """
        Append a song to the playlist.
        >>> pl = Playlist()
        >>> pl.append_song(Song('Sandstorm', 'Darude', 255))
        >>> pl
        [Song('Sandstorm', 'Darude', 255)]
        """
        self.songs.append(new_song)
        
    def get_songs_as_strings(self) -> list[str]:
        """
        Get a list of strings representing the songs in the playlist.
        >>> pl = Playlist()
        >>> pl.append_song(Song('Sandstorm', 'Darude', 255))
        >>> pl.get_songs_as_strings()
        ['Sandstorm by Darude, 255 seconds long']
        """
        list_of_strings = []
        
        for song in self.songs:
            list_of_strings.append(str(song))
            
        return list_of_strings        
        
    def get_playlist_length(self) -> int:
        """
        Get the total length of all of the songs the playlist.
        >>> pl1 = Playlist()
        >>> pl1.get_playlist_length()
        0
        >>> pl2 = Playlist()
        >>> pl2.append_song(Song('song 1', 'artist', 1))
        >>> pl2.append_song(Song('song 2', 'artist', 1))
        >>> pl2.get_playlist_length()
        2
        """
        length = 0
        
        for song in self.songs:
            length += song.get_length()
        return length
    
    def get_playlist_as_list_of_lists(self) -> list[list]:
        """
        Get the playlist, represented as a list of lists.
        >>> pl2 = Playlist()
        >>> pl2.append_song(Song('song 1', 'artist', 1))
        >>> pl2.append_song(Song('song 2', 'artist', 1))
        >>> pl2.get_playlist_as_list_of_lists()
        [['song 1', 'artist', 1], ['song 2', 'artist', 1]]
        """
        list_of_lists = []
        
        for song in self.songs:
            list_of_lists.append([song.get_title(), 
                                  song.get_artist(), 
                                  song.get_length()])
        
        return list_of_lists            