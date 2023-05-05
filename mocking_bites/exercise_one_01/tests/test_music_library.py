from lib.music_library import *
from unittest.mock import Mock

def test_initialises_library():
    library = MusicLibrary()
    assert library.list_tracks == []

def test_track_gets_added_to_library():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.title.return_value = 'You First'
    track_1.artist.return_value = 'Paramore'
    library.add(track_1)
    assert library.list_tracks == [track_1]

def test_search_returns_track():
    library = MusicLibrary()
    track_1 = Mock()
    track_2 = Mock()
    # track_1.title.return_value = 'You First'
    # track_1.artist.return_value = 'Paramore'
    # track_2.title.return_value = 'Figure 8'
    # track_2.artist.return_value = 'Paramore'
    library.add(track_1)
    library.add(track_2)
    track_1.matches.return_value = True
    track_2.matches.return_value = True
    assert library.search('Paramore') == [track_1, track_2]
