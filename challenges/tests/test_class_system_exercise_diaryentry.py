from lib.class_system_exercise_diaryentry import *
import pytest

def test_constructs_and_gets_title_and_contents():
    my_diary = DiaryEntry("Monday", 'Today was a great day.')
    assert my_diary.title == 'Monday'
    assert my_diary.contents == 'Today was a great day.'

def test_word_count():
    entry1 = DiaryEntry('Monday', 'Today is a bank holiday.')
    entry2 = DiaryEntry('Tuesday', 'It is rainy today.')
    assert entry1.count_words() == 5
    assert entry2.count_words() == 4