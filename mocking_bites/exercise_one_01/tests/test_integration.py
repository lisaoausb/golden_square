from lib.music_library import *
from lib.track import *
import pytest

def test_adds_track_to_library():
    library = MusicLibrary()
    track_1 = Track('You First', 'Paramore')
    track_2 = Track("Can't help mysef", "The Kelly Family")
    track_3 = Track("This is a very long title", 'By an artist we do not know')
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.list_tracks == [track_1, track_2, track_3]

def test_searches_artist_in_library():
    library = MusicLibrary()
    track_1 = Track('You First', 'Paramore')
    track_2 = Track("Can't help mysef", "The Kelly Family")
    track_3 = Track("This is a very long title", 'By an artist we do not know')
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.search('Paramore') == [track_1]

def test_searches_title_in_library():
    library = MusicLibrary()
    track_1 = Track('You First', 'Paramore')
    track_2 = Track("Can't help mysef", "The Kelly Family")
    track_3 = Track("This is a very long title", 'By an artist we do not know')
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.search('very long') == [track_3]

def test_searches_keyword_in_library_that_is_not_found():
    library = MusicLibrary()
    track_1 = Track('You First', 'Paramore')
    track_2 = Track("Can't help mysef", "The Kelly Family")
    track_3 = Track("This is a very long title", 'By an artist we do not know')
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.search('Led Zeppelin') == []

def test_same_keyword_in_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track('You First', 'Paramore')
    track_2 = Track("Can't help mysef", "The Kelly Family")
    track_3 = Track("This is a very long title", 'By an artist we do not know')
    track_4 = Track("We are Family", 'Unknown')
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    library.add(track_4)
    assert library.search('Family') == [track_2, track_4]
