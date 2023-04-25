from lib.diary import *

def test_empty_string():
    test = make_snippet("")
    assert test == ""

def test_make_short_snippet():
    test = make_snippet("Dear Diary. Absolutely no comment.")
    assert test == 'Dear Diary. Absolutely no comment.'

def test_make_long_snippet():
    test = make_snippet('Dear Diary. Today I spent five hours working on one challenge.')
    assert test == 'Dear Diary. Today I spent ...'

# 02_test_drive_a_single_function.md
# Challenge

def test_count_words():
    word_count = count_words("How many words do I have")
    assert word_count == 6

def test_0_count():
    word_count = count_words('')
    assert word_count == 0