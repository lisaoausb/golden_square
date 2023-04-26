import pytest
from lib.design_challenge import *

"""
Given a string that contains #TODO
Return True
"""
def test_text_contains_hashtag_todo():
    result = track_tasks('#TODO: do challenge')
    assert result == True

"""
Given a string that does not contain #TODO
Return False
"""
def test_text_does_not_contain_hashtag_todo():
    result = track_tasks('do challenge')
    assert result == False

"""
Given an empty string
Return error: 'No task given.'
"""
def test_no_text_given():
    with pytest.raises(Exception) as e: 
        result = track_tasks('')
    error = str(e.value)
    assert error == 'No task given.'
