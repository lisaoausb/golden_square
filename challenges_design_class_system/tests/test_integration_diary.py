from lib.diary import *
from lib.diaryentry import *
from lib.phonenumbers import *
from lib.readingextractor import *


# INTEGRATION TESTS – DIARY, DIARYENTRY, READINGEXTRACTOR, PHONENUMBERS

"""
Initially
Adding multiple entries
Returns list of entries
"""
def test_multiple_entries_return_list():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1")
    entry_2 = DiaryEntry("Entry 2", "Content 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Initially
Adding multiple entries
Returns number of words in all diary entries
"""
def test_word_number_with_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1")
    entry_2 = DiaryEntry("Entry 2", "Content 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 4

"""
Initially
Adding multiple diary entries
Return integer representing reading time in minutes
"""
def test_reading_time_in_minutes_with_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1")
    entry_2 = DiaryEntry("Entry 2", "Content 2 one two three four")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 6

"""
Initially
Adding multiple diaries, wpm and minutes
Return None if no instance of a diary representing the entry fits the time available (i.e. all entries take longer to read than the time we have)
"""

def test_reading_time_in_minutes_returns_None():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1")
    entry_2 = DiaryEntry("Entry 2", "Content 2 five six seven eight")
    entry_3 = DiaryEntry("Entry 3", "Content 3 five six seven eight nine ten")
    diary.add(entry_1)
    diary.add(entry_3)
    diary.add(entry_2)
    reader = ReadingExtractor(diary)
    assert reader.find_best_entry_for_reading_time(1, 1) == None

"""
Initially
Adding multiple diaries, wpm and minutes
Return an instance of a diary representing the entry that is closest to the time the user has to read, but not over
"""

def test_reading_time_in_minutes_with_multiple_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1")
    entry_2 = DiaryEntry("Entry 2", "Content 2 five six seven eight")
    entry_3 = DiaryEntry("Entry 3", "Content 3 five six seven eight nine ten")
    diary.add(entry_1)
    diary.add(entry_3)
    diary.add(entry_2)
    reader = ReadingExtractor(diary)
    assert reader.find_best_entry_for_reading_time(2, 4) == entry_3


"""
Initially
Adding a diary (class) instance with several entries not containing phone numbers
Return a list of phone numbers
"""

def test_get_empty_list_if_no_phone_numbers_in_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1 does not have a phone number")
    entry_2 = DiaryEntry("Entry 2", "Content 2 contains no dummy number")
    entry_3 = DiaryEntry("Entry 3", "Content 3 cannot be reached at the minute")
    diary.add(entry_1)
    diary.add(entry_3)
    diary.add(entry_2)
    contacts = PhoneNumbers(diary)
    result = contacts.see_numbers()
    assert result == []


"""
Initially
Adding a diary (class) instance with several entries containing phone numbers
Return a list of phone numbers
"""

def test_get_list_of_phone_numbers_from_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Entry 1", "Content 1 does not have a phone number")
    entry_2 = DiaryEntry("Entry 2", "Content 2 contains the following dummy number: 07582927564")
    entry_3 = DiaryEntry("Entry 3", "Content 3 can be reached under 07809123123 or 07923345345")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    contacts = PhoneNumbers(diary)
    assert contacts.see_numbers() == ['07582927564', '07809123123', '07923345345']