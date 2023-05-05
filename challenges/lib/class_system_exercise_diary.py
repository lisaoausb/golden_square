from lib.class_system_exercise_diaryentry import *
import math

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        self._entries.append(entry)
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._entries

    def count_words(self):
        # for entry in self._entries:
        #     self._word_count += entry.count_words()
        # return self._word_count
        # => the above created a problem with reading time when count_words
        # was not specifically called first 
    
        return sum([entry.count_words() for entry in self._entries])
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if self.count_words() == 0:
            raise Exception("No entries to read available")
        else:
            return math.ceil(self.count_words()/wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        if self._entries == []:
            return None
        else: 
            for entry in self._entries:
                if entry.count_words() / wpm <= minutes:
                    return entry
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.