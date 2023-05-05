class ReadingExtractor():

    def __init__(self, diary):
        self.diary = diary
        # Parameters: an instance of the diary class
        # Returns: none
        # Side effects: set up diary property 
        # self.diary = diary

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self.diary.entries:
            if entry.count_words() <= words_user_could_read:
                if entry.count_words() > longest_found_so_far:
                        most_readable = entry
                        longest_found_so_far = entry.count_words()
        return most_readable
    
    # Parameters: my reading speed and my time available
        # Returns: Entry that I can read during this time at this pace
        # Side effects: saves my progress so I can continue where I left off
            # // need word count of entries and time it takes to read

        # need to iterate over individual entries in my diary instances
        # for entry in self.diary.entries