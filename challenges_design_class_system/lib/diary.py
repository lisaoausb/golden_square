class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries
    
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        # words = ""
        total_words = 0
        for entry in self.entries:
            total_words += entry.count_words()
            # words += f'{entry._title}: {entry._contents} '
        # return len(words.split())
        return total_words
