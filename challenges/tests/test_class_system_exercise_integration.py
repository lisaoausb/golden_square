from lib.class_system_exercise_diary import *
from lib.class_system_exercise_diaryentry import *
import pytest
""""
kdgjopweg
"""
def test_adds_multiple_entries_and_lists_them():
    my_diary = Diary()
    entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
    entry2 = DiaryEntry("Tuesday", 'Today was a much better day.')
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.all() == [entry1, entry2]

def test_returns_word_count_of_multiple_entries():
    my_diary = Diary()
    entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
    entry2 = DiaryEntry("Tuesday", 'Today was a much better day.')
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.count_words() == 13

def test_reading_time_of_two_entries():
    my_diary = Diary()
    entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
    entry2 = DiaryEntry("Tuesday", 'Today was a much better day.')
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.reading_time(2) == 7

def test_reading_time_of_two_entries_while_calling_word_count():
    my_diary = Diary()
    entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
    entry2 = DiaryEntry("Tuesday", 'Today was a much better day.')
    my_diary.add(entry1)
    my_diary.add(entry2)
    my_diary.count_words()
    assert my_diary.reading_time(2) == 7

def test_best_entry_for_reading_time_one_in_boundary():
    my_diary = Diary()
    entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
    entry2 = DiaryEntry("Tuesday", 'Today was a much better day.')
    my_diary.add(entry1)
    my_diary.add(entry2)
    assert my_diary.find_best_entry_for_reading_time(2, 3) == entry2

# def test_best_entry_for_reading_time_two_in_boundary_longest():
#     my_diary = Diary()
#     entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
#     entry2 = DiaryEntry("Tuesday", 'Today was a much better day, hell yeah.')
#     my_diary.add(entry1)
#     my_diary.add(entry2)
#     assert my_diary.find_best_entry_for_reading_time(2, 4) == entry2

# def test_best_entry_for_reading_time_two_in_boundary_and_same():
#     my_diary = Diary()
#     entry1 = DiaryEntry('Monday', 'What happened today was not very nice.')
#     entry2 = DiaryEntry("Tuesday", 'What happened today was indeed very nice.')
#     my_diary.add(entry1)
#     my_diary.add(entry2)
#     assert my_diary.find_best_entry_for_reading_time(2, 4) == [entry1, entry2]