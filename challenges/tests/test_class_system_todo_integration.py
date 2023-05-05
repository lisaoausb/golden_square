from lib.class_system_todo import *
from lib.class_system_todo_list import *
import pytest

'''
Given I add two tasks,
I do not complete any of them and get them returned in list of 
incomplete tasks
'''

def test_multiple_tasks_added_to_incomplete_list():
    list = TodoList()
    task_1 = Todo("Do the laundry")
    task_2 = Todo("Water the flowers")
    list.add(task_1)
    list.add(task_2)
    assert list.incomplete() == [task_1, task_2]

def test_multiple_tasks_completed_added_to_complete_list():
    list = TodoList()
    task_1 = Todo("Do the laundry")
    task_2 = Todo("Water the flowers")
    list.add(task_1)
    list.add(task_2)
    task_1.mark_complete()
    print(task_1.completed)
    task_2.mark_complete()
    print(task_2.completed)
    list.complete()
    assert list._completes == [task_1, task_2]

def test_some_tasks_complete_some_incomplete():
    list = TodoList()
    task_1 = Todo("Do the laundry")
    task_2 = Todo("Water the flowers")
    list.add(task_1)
    list.add(task_2)
    task_1.mark_complete()
    list.incomplete()
    list.complete()
    assert list._incompletes == [task_2]
    assert list._completes == [task_1]

def test_give_up_on_tasks():
    list = TodoList()
    task_1 = Todo("Do the laundry")
    task_2 = Todo("Water the flowers")
    list.add(task_1)
    list.add(task_2)
    list.give_up()
    assert list._completes == [task_1, task_2]

def test_give_up_with_existing_completes():
    list = TodoList()
    task_1 = Todo('Do the laundry')
    task_2 = Todo('Water the flowers')
    list.add(task_1)
    list.add(task_2)
    task_2.mark_complete()
    list.complete()
    list.give_up()
    assert list._completes == [task_2, task_1]

def test_give_up_with_existing_completes_three():
    list = TodoList()
    task_1 = Todo('Do the laundry')
    task_2 = Todo('Water the flowers')
    task_3 = Todo('Do my homework')
    list.add(task_1)
    list.add(task_2)
    list.add(task_3)
    task_2.mark_complete()
    list.complete()
    list.give_up()
    assert list._completes == [task_2, task_1, task_3]