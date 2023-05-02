from lib.design_class_exercise import *
import pytest

def test_task_added_successfully():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    number_of_tasks = len(tracker.tasks)
    assert number_of_tasks == 1

def test_see_list_of_two_tasks():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    task_list = tracker.see_tasks()
    assert task_list == 'Your tasks: sort out wardrobe, practise songs for wedding'

def test_see_list_of_one_task_after_completing_another():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    tracker.mark_task_complete('Practise songs for wedding')
    task_list = tracker.see_tasks()
    assert task_list == 'Your tasks: sort out wardrobe'

def test_see_list_of_one_task_after_completing_another_case_mismatch():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    tracker.mark_task_complete('practise songs for wedding')
    task_list = tracker.see_tasks()
    assert task_list == 'Your tasks: sort out wardrobe'

def test_see_list_but_no_tasks():
    tracker = TaskTracker('Lisa')
    task_list = tracker.see_tasks()
    assert task_list == "You're all caught up, Lisa."

def test_mark_misspelt_or_nonexisting_task_complete_on_nonempty_list():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    with pytest.raises(Exception) as e:
        tracker.mark_task_complete('Practice songs for wedding')
    error = str(e.value)
    assert error == 'No such task found. Check your spelling, Lisa, or see the list of tasks: sort out wardrobe, practise songs for wedding'

def test_mark_task_complete_on_empty_list():
    tracker = TaskTracker('Lisa')
    with pytest.raises(Exception) as e:
        tracker.mark_task_complete('Practice songs for wedding')
    error = str(e.value)
    assert error == 'Your list is empty, Lisa.'