from lib.class_system_exercise_diary import *
import pytest

def test_initially_has_empty_list():
    my_diary = Diary()
    assert my_diary.all() == []

def test_intially_word_count_is_zero():
    my_diary = Diary()
    assert my_diary.count_words() == 0

def test_raise_error_when_no_entries_given():
    my_diary = Diary()
    with pytest.raises(Exception) as e:
        my_diary.reading_time(2)
    error = str(e.value)
    assert error == 'No entries to read available'

def test_return_none_if_no_reading_time():
    my_diary = Diary()
    assert my_diary.find_best_entry_for_reading_time(2,2) == None