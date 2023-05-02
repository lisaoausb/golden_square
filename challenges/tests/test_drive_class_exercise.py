import pytest
from lib.drive_class_exercise import *

# """
# As a user
# To create diary entries and read them based on the number of 
# words and reading time. The user also wants to be able to continue
# where they left off.
# """


# """
# Given a diary entry and return title and contents in a nicely formatted style.
# """
# def test_format_of_entry():
#     entry260423 = DiaryEntry('Entry 26/04/23', 'This is the entry from Wednesday, 26/04/23.')
#     result = entry260423.format()
#     assert result == "Entry 26/04/23: This is the entry from Wednesday, 26/04/23."
    

# """
# Given a diary entry with a title and contents
# #count_words returns the number of words of the diary entry
# """ 
# def test_count_words_of_entry():
#     entry260423 = DiaryEntry('Entry 26/04/23', 'This is the entry from Wednesday, 26/04/23.')
#     result = entry260423.count_words()
#     assert result == 9  

# def test_count_words_of_empty_entry():
#     with pytest.raises(Exception) as e:
#         DiaryEntry("","")
#     error = str(e.value)
#     assert error == "Entry can't be empty."

# """
# Given a wpm of 2 and contents with 2 words,
# #reading_time returns a reading time of 1 minute.
# """
# def test_reading_time_of_two_words_is_one_minute():
#     entry = DiaryEntry('The title', 'Two words')
#     result = entry.reading_time(2)
#     assert result == 1

# """
# Given a wpm of 2 and contents with 3 words,
# #reading_time returns a reading time of 1 minute.
# """
# def test_reading_time_of_three_words_is_one_half_minute():
#     entry = DiaryEntry('The title', 'Three words here')
#     result = entry.reading_time(2)
#     assert result == 2


# # """
# # Given a wpm of 2 and contents with 3 words,
# # #reading_time returns a reading time of 1 minute.
# # """
# # def test_reading_time_of_empty_string_throws_error():
# #     with pytest.raises(Exception) as e:
# #         entry = DiaryEntry('The title', '')
# #         result = entry.reading_time(2)
# #     error = str(e.value)
# #     assert error == "Entry can't be empty."

# """
# Given a diary entry of 500 words with a reading time of 200 pmw. We have 2 minutes
# to read and so have to come back for 1 minute (100 words).
# """

#  entry260423.reading_time(200)
#     assert entry260423.reading_chunk(200,2) == (print('hi') for i in range(0,400))

# tests from exercise from pairing
import pytest
from lib.drive_class_exercise import *
"""Given a title and contents, format the entry like this: "My Title: These are the contents."""
def test_empty_string():
    with pytest.raises(Exception) as e:
        DiaryEntry("", "")
    assert str(e.value) == "Please enter a title and contents."
""" Formats the title and contents as "My Title: These are the contents"""
def test_format_diary():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.format()
    assert result == "My Title: These are the contents"
"""returns the number of words in the entry."""
def test_count_words():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.count_words()
    assert result == 6
"""Given a reading speed in words per minute, it returns how long it would take to read the entry."""
def test_reading_time():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.reading_time(6)
    assert result == 1
"""Given a wpm and a number of minutes, it returns a chunk of text that could be read in that time."""
def test_reading_time_with_number_not_whole():
    diary = DiaryEntry("My Title", "These")
    result = diary.reading_time(2)
    assert result == 1
"""Given a wpm of 2 and a number of minutes of 1, it returns a chunk of text that could be read."""
def test_reading_chunk():
    diary = DiaryEntry("My Title", "These are the contents")
    result = diary.reading_chunk(2, 1)
    assert result == "My Title:"
def test_reading_chunk_two_entries():
    diary = DiaryEntry("My Title", "These are the contents")
    assert diary.reading_chunk(3,1) == "My Title: These"
    assert diary.reading_chunk(3,1) == "are the contents"
def test_reading_chunk_looping_round():
    diary = DiaryEntry("My Title", "These are the contents")
    assert diary.reading_chunk(3,1) == "My Title: These"
    assert diary.reading_chunk(3,1) == "are the contents"
    assert diary.reading_chunk(3,1) == "My Title: These"