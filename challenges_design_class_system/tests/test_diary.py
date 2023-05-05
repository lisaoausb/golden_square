from lib.diary import *

"""
Initially, 
diary.entries list is empty because we haven't passed any instances of DiaryEntry yet
"""

def test_list_of_entries_is_empty():
    diary = Diary()
    assert diary.entries == []

"""
Initially,
diary.all returns an empty list because we haven't passed any diary entries
"""

def test_returns_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []