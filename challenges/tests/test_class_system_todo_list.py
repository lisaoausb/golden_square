from lib.class_system_todo_list import *
import pytest

"""
Initially, I have an empty list of incomplete tasks
Return error message
"""

def test_incompletes_is_empty():
    list = TodoList()
    with pytest.raises(Exception) as e:
        list.incomplete()
    assert str(e.value) == 'No outstanding tasks'

"""
Initially, I have an empty list of complete tasks
Return error message
"""

def test_completes_is_empty():
    list = TodoList()
    with pytest.raises(Exception) as e:
        list.complete()
    assert str(e.value) == 'No tasks completed yet'
