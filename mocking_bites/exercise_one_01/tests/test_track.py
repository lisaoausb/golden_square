from lib.track import *

def test_initialises_track():
    track_1 = Track('You First', "Paramore")
    assert track_1.title == 'You First'
    assert track_1.artist == 'Paramore'

def test_matching_keyword_returns_True():
    track_1 = Track("You First", "Paramore")
    assert track_1.matches('First') == True
    assert track_1.matches('Business') == False