import math

# class DiaryEntry:
#     def __init__(self, title, contents):
#         if title == "" or contents == "":
#             raise Exception("Entry can't be empty.")
#         self._title = title
#         self._contents = contents
#         # Parameters:
#         #   title: string
#         #   contents: string
    

#     def format(self):
#         return f"{self._title}: {self._contents}"

#     def count_words(self):
#         words = self.format().split()
#         word_count = len(words)
#         return word_count
#         # Returns:
#         #   int: the number of words in the diary entry

#     def reading_time(self, wpm):
#         # Parameters:
#         #   wpm: an integer representing the number of words the user can read 
#         #        per minute
#         # Returns:
#         #   int: an estimate of the reading time in minutes for the contents at
#         #        the given wpm.
#         word_count = len(self._contents.split())
#         return math.ceil(word_count / wpm)

#     def reading_chunk(self, wpm, minutes):
#         # Parameters
#         #   wpm: an integer representing the number of words the user can read
#         #        per minute
#         #   minutes: an integer representing the number of minutes the user has
#         #            to read
#         # Returns:
#         #   string: a chunk of the contents that the user could read in the
#         #           given number of minutes
#         #
#         # If called again, `reading_chunk` should return the next chunk,
#         # skipping what has already been read, until the contents is fully read.
#         # The next call after that should restart from the beginning.
#         pass

# solution from pairing

import math
class DiaryEntry():
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Please enter a title and contents.")
        self.title = title
        self.contents = contents
        self.read_so_far = 0
    def format(self):
        return f"{self.title}: {self.contents}"
    
    def count_words(self):
        count = self.format().split()
        return len(count)
    
    def reading_time(self, wpm):
        length = len(self.contents.split())
        return math.ceil(length/wpm)
    def reading_chunk(self, wpm, minutes):
        amount_of_words = wpm * minutes
        text = self.format().split()
        if self.read_so_far >= len(text):
            self.read_so_far = 0
        chunk_start = self.read_so_far 
        chunk_end = self.read_so_far + amount_of_words
        chunk = text[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk)