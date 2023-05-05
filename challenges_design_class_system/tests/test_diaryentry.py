import pytest
from lib.diaryentry import *

"""
When I initialise without a title and contents
I get an error message
"""
def test_contstructs_and_gets_no_title_and_no_contents():
      with pytest.raises(Exception) as e:
          diary_entry = DiaryEntry("", "")
      error = str(e.value)
      assert error == "Diary entries must have a title and contents"

"""
When I initilalise with a title and contents
I can get that title and contents back
"""
def test_contstructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"
"""
Initially
Adding one entry
Return the length of words in the entry
"""
def test_when_adding_one_entry_returns_number_of_words():
    diary = DiaryEntry("Title 1", "Content 1")
    assert diary.count_words() ==  2
