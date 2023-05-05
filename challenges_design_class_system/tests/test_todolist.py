from lib.todolist import *
import pytest

"""
Initially, I have an empty list of incomplete tasks
Return error message
"""

def test_incompletes_is_empty():
    list = TodoList()
    assert list.incomplete() == []

"""
Initially, I have an empty list of complete tasks
Return error message
"""

def test_completes_is_empty():
    list = TodoList()
    assert list.complete() == []
