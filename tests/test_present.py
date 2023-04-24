import pytest
from lib.present import *

"""
we wrap a present and get it back when unwrapping
"""

def test_wrap_and_unwrap():
    present = Present()
    present.wrap(12345)
    result = present.unwrap()
    assert result == 12345

# wrap already wrapped
# need a further test to make sure present is not overwritten

def test_wrap_error():
    present = Present()
    present.contents = 'not empty'
    with pytest.raises(Exception) as e:
        present.wrap('new content')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# we unwrap before we wrap, so get an error

def test_unwrap_error():
    present = Present()
    present.contents = None
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
