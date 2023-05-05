import re

class PhoneNumbers():
    # User-facing properties:
    # List of phone numbers

    def __init__(self, diary):
        # Parameters: the diary I want phone numbers from
        # Returns nothing
        # Side effects: sets up a phone number list
        self.diary = diary
        self.phone = []

    def see_numbers(self):
        # Parameters: none
        # Returns: a list of phone numbers
        # side effects: none
        # Needs to iterate over self.diary.entries and find numbers in contents of individual entries and add them to the list,
        # finally returns said list
        for entry in self.diary.entries:
            my_string = entry.contents
            number = re.findall(r'\b\d{11}\b', my_string) # Output: ['12345678901', '98765432109']
            self.phone += number

        # unique_numbers = [*set(self.phone)]

        if len(self.phone) > 0:
            return self.phone
        else:
            return self.phone
        
        
        
