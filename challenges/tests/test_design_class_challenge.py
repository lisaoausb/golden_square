import pytest
from lib.design_class_challenge import *

"""
Given an empty string as track
Returns error message
"""

def test_error_if_song_is_empty_string():
    playlist = MusicTracker()
    with pytest.raises(Exception) as e:
        playlist.add_song("")
    error = str(e.value)
    assert error == 'Song cannot be empty'

"""
Given a song
Song is added to list and list has 1 value
"""

def test_song_added_to_list():
    playlist = MusicTracker()
    playlist.add_song("Invierno porteño")
    result = len(playlist.songs)
    assert result == 1

"""
Given no songs, list is empty
Returns error message
"""

def test_error_if_list_is_empty():
    playlist = MusicTracker()
    with pytest.raises(Exception) as e:
        playlist.see_list()
    error = str(e.value)
    assert error == 'You have not listened to any songs'

"""
Given two songs, songs are added to list
Returns list of songs
"""

def test_songs_returned_in_list():
    playlist = MusicTracker()
    playlist.add_song("Invierno porteño")
    playlist.add_song("You First")
    result = playlist.see_list()
    assert result == ["Invierno porteño", "You First"]