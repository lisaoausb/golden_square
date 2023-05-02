MUSIC TRACKING Class Design Recipe

1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class MusicTracker:
    # None

    def __init__(self):
        # Parameters: none
        # Side effects: keeps a list of songs that will be added to
        pass 

    def add_song(self, song):
        # Parameters: takes a song I have listened to, string
        # Returns: nothing
        # Side effects: adds to the list in the initialiser
        pass; throws an error if string is empty

    def see_list(self):
        # Parameters: none
        # Returns: list of songs
        # Side effects: throws an error if list is empty

3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

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

    

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.