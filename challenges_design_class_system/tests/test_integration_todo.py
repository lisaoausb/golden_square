from lib.todo import *
from lib.todolist import *
import pytest 

# INTEGRATION TESTS – TASKLIST AND TASKS

"""
Initially
Given one task
Returns the task as incomplete
"""
def test_when_given_one_task_and_not_completed_it_returns_as_incomplete():
    to_do = TodoList()
    task_1 = Todo("task 1")
    to_do.add(task_1)
    assert to_do.incomplete() == [task_1]
"""
Initially
Given multiple tasks
Returns the tasks as incomplete
"""
def test_when_given_multiple_tasks_returns_them_as_incomplete():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    to_do.add(task_1)
    to_do.add(task_2)
    assert to_do.incomplete() == [task_1, task_2]
"""
Initially
Given two tasks and marking none of them as complete
Returns empty list
"""
def test_when_two_tasks_not_marked_as_complete_returns_empty_list():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    to_do.add(task_1)
    to_do.add(task_2)
    assert to_do.complete() == []

"""
Initially
Given three tasks and marking two as complete
Returns two tasks that were completed and one task incompleted
"""
def test_when_given_multiple_tasks_returns_the_completed_one():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    task_3 = Todo("task 3")
    to_do.add(task_1)
    to_do.add(task_2)
    to_do.add(task_3)
    task_2.mark_complete()
    task_3.mark_complete()
    assert to_do.complete() == [task_2, task_3]
    assert to_do.incomplete() == [task_1]
"""
Initially
Given three tasks and marking two as complete and then give up
Check returns all as completed
"""
def test_when_given_multiple_tasks_not_all_complete_and_give_up():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    task_3 = Todo("task 3")
    to_do.add(task_1)
    to_do.add(task_2)
    to_do.add(task_3)
    task_2.mark_complete()
    task_3.mark_complete()
    to_do.give_up()
    result = to_do.complete()
    assert result == [task_1, task_2, task_3]