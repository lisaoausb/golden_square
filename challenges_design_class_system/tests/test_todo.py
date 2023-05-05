from lib.todo import *
import pytest
"""
Given a task,
adds task properties and gives us the task status which is False (i.e. incomplete)
"""

def test_see_status_of_task():
    task_1 = Todo("Do the laundry")
    assert task_1.complete == False

"""
Given a task,
we mark it complete and its status changes to True (i.e. complete)
"""

def test_mark_task_complete():
    task_1 = Todo("Do the laundry")
    task_1.mark_complete()
    assert task_1.complete == True