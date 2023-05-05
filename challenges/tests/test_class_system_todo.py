from lib.class_system_todo import *
import pytest

"""
Given a task,
adds task
"""

def test_see_status_of_task():
    task_1 = Todo("Do the laundry")
    assert task_1.completed == False

def test_mark_task_complete():
    task_1 = Todo("Do the laundry")
    assert task_1.completed == False
    task_1.mark_complete()
    assert task_1.completed == True