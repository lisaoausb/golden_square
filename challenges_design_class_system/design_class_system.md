EXPERIENCES/DIARY/TASKS
Multi-Class Planned Design Recipe

1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

2. Design the Class System

Consider diagramming out the classes and their relationships. Take care to focus on the details you see as important, not everything. The diagram below uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com

![Afzaa's and my design](Untitled-2023-05-03-1245.png)


My design alone, little bit of video input (task and diary separated)

                     ┌──────────────────────────────┐       ┌───────────┐
                     │                              │       │           │
                     │                              │       │           │
                     │   This is the DIARY class    │       │  TaskList │
          ┌─────────►│                              │       │           │
          │          │                              │       │           │
          │          │                              │       │           │
          │          └──────▲───────────────────────┘       └─────┬─────┘
          │                 │                                     │
  ┌───────┴────┐     ┌──────┴─────┐                               │
  │            │     │            │                         ┌─────▼─────┐
  │ DiaryEntry │     │   Numbers  │                         │           │
  │  to store  │◄────┤   to store │                         │           │
  │   entries  │     │ phone nrs  │                         │ TaskEntry │
  │            │     │            │                         │           │
  └────────────┘     └────────────┘                         │           │
                                                            └───────────┘


Also design the interface of each class in more detail.

class Diary:
    # User-facing properties:
    #   entries: list of instances of DiaryEntry

def __init__(self):
    # Parameters: none
    # Returns: none
    # Side effects: need a list property to store all diary entries in
    self.entries = entries
    pass 

def add(self, entry):
    # Parameters: Diary entry
    # Returns: nothing
    # Side effects: adds diary entry to list (property)

<!-- def read(self, title):
    # Parameters: title (?? to access contents of specific entry I want to read??)
    # Returns: self.contents
    # Side effects: none -->

def all(self):
    # Parameters: none
    # Returns: list of entries (title and contents) -- in a nice format?
    # Side effects: none

def count_words(self):
    # Parameters: none
    # Returns: number of words in self.contents
    # Side effects: uses the count_words method from DiaryEntry
        pass

class DiaryEntry:
    # User-facing properties:
    #   none?

    def __init__(self, title, contents):
        # Parameters: title (string) and content (string) of diary entry
        # Returns: Nothing
        # Side effects: sets title and contents properties
        self.title = title
        self.contents = contents
        pass
    
    def count_words(self):
        # Parameters: none
        # Returns: number of words in self.contents
        # Side effects: none / return can be used in other places
        pass
    
<!-- def reading_time(self, wpm):
        # Parameters: words per minute user can read
        # Returns: minutes it takes to read contents 
        # Side effects: none / return can be used in other places
        # Note: can use #count_words in here??
        pass -->

<!-- def format(self):
        # Parameters: none
        # Returns: none
        # Side effects: puts entry in a nice format -->

class ReadingExtractor():

    def __init__(self, diary):
        # Parameters: an instance of the diary class
        # Returns: none
        # Side effects: set up diary property 
        # self.diary = diary

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters: my reading speed and my time available
        # Returns: Entry that I can read during this time at this pace
        # Side effects: saves my progress so I can continue where I left off
            // need word count of entries and time it takes to read

        # need to iterate over individual entries in my diary instances
        # for entry in self.diary.entries


class TodoList():
    # User-facing properties: 
    #   tasks: list of entries in TaskEntry

    def __init__(self):
        # Parameters: none
        # Returns: nothing
        # Side effects: need a list property to store all tasks in
            pass
    
    def add(self, task):
        # Parameters: task entry
        # Returns: nothing
        # Side effects: adds task to list

    def incomplete(self):
        # Parameters: none
        # Returns: list of all tasks in my to-do list that are incomplete
        # Side effects: none
        pass

    def complete(self):
        # Parameters: none
        # Returns: list of all tasks in my to-do list that are complete
        # Side effects: none
    
    def give_up(self):
        # Parameters: none
        # Returns: none
        # Side effects: marks all incomplete tasks as complete

class Todo():
    # User-facing properties:
    # none?

    def __init__(self, task):
        # Parameters: task (string)
        # Returns: nothing
        # Side effects: sets task property, sets task status as False for incomplete
        # self.task = task
        # self.completed = False


    def mark_complete(self):
        # Parameters: none
        # Returns: nothing
        # Side effects: sets status to True for complete 


class PhoneNumbers():
    # User-facing properties:
    # List of phone numbers

    def __init__(self, diary):
        # Parameters: the diary I want phone numbers from
        # Returns nothing
        # Side effects: sets up a phone number list
        # self.diary = diary
        # self.phone = []

    def see_numbers(self):
        # Parameters: none
        # Returns: a list of phone numbers
        # side effects: none
        # Needs to iterate over self.diary.entries and find numbers in contents of individual entries and add them to the list,
        # finally returns said list


3. Create Examples as Integration Tests

Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

INTEGRATION TESTS – DIARY, DIARYENTRY, READINGEXTRACTOR, PHONENUMBERS

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
    assert diary.count_words() == 8

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
    assert contacts.see_numbers() == []


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
    diary.add(entry_3)
    diary.add(entry_2)
    contacts = PhoneNumbers(diary)
    assert contacts.see_numbers() == ['07582927564', '07809123123', '07923345345']

INTEGRATION TESTS – TASKLIST AND TASKS

"""
Initially
Given one task
Returns the task as incomplete
"""
def test_when_given_one_task_and_not_completed_it_returns_as_incomplete():
    to_do = TodoList()
    task_1 = Todo("task 1")
    to_do.add(task_1)
    assert to_do.incomplete() == [task_1]
"""
Initially
Given multiple tasks
Returns the tasks as incomplete
"""
def test_when_given_multiple_tasks_returns_them_as_incomplete():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    to_do.add(task_1)
    to_do.add(task_2)
    assert to_do.incomplete() == [task_1, task_2]
"""
Initially
Given two tasks and marking none of them as complete
Returns empty list
"""
def test_when_two_tasks_not_marked_as_complete_returns_empty_list():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    to_do.add(task_1)
    to_do.add(task_2)
    assert to_do.complete() == []
"""
Initially
Given three tasks and marking two as complete
Returns two tasks that were completed and one task incompleted
"""
def test_when_given_multiple_tasks_returns_the_completed_one():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    task_3 = Todo("task 3")
    to_do.add(task_1)
    to_do.add(task_2)
    to_do.add(task_3)
    task_2.mark_complete()
    task_3.mark_complete()
    assert to_do.complete() == [task_2, task_3]
    assert to_do.incomplete() == [task_1]
"""
Initially
Given three tasks and marking two as complete and then give up
Check returns all as completed
"""
def test_when_given_multiple_tasks_not_all_complete_and_give_up():
    to_do = TodoList()
    task_1 = Todo("task 1")
    task_2 = Todo("task 2")
    task_3 = Todo("task 3")
    to_do.add(task_1)
    to_do.add(task_2)
    to_do.add(task_3)
    task_2.mark_complete()
    task_3.mark_complete()
    to_do.give_up()
    assert to_do.complete() == [task_1, task_2, task_3]

12 integration tests

UNIT TESTS

1. Diary

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


2. DiaryEntry

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

"""
When I initialise without a title and contents
I get an error message
"""
def test_contstructs_and_gets_no_title_and_no_contents():
    with pytest.raises(Exception) as e:
        diary_entry = DiaryEntry("", "")
    error = str(e.value)
    assert error == "Diary entries must have a title and contents"


3. ReadingExtractor

"""
Would have to use Mock() here to do unit-testing, but will skip as it is out of scope for this exercise.
"""

4. TodoList
"""
Initially, I have an empty list of incomplete tasks
Return error message
"""

def test_incompletes_is_empty():
    list = TodoList()
    with pytest.raises(Exception) as e:
        list.incomplete()
    assert str(e.value) == 'No outstanding tasks'

"""
Initially, I have an empty list of complete tasks
Return error message
"""

def test_completes_is_empty():
    list = TodoList()
    with pytest.raises(Exception) as e:
        list.complete()
    assert str(e.value) == 'No tasks completed yet'

5. Todo

"""
Given a task,
adds task properties and gives us the task status which is False (i.e. incomplete)
"""

def test_see_status_of_task():
    task_1 = Todo("Do the laundry")
    assert task_1.completed == False

"""
Given a task,
we mark it complete and its status changes to True (i.e. complete)
"""

def test_mark_task_complete():
    task_1 = Todo("Do the laundry")
    task_1.mark_complete()
    assert task_1.completed == True

6. PhoneNumbers
"""
Would have to use Mock() here to do unit-testing, but will skip as it is out of scope for this exercise.
"""

8 unit tests


20 total tests


# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
4. Create Examples as Unit Tests

Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
Encode each example as a test. You can add to the above list as you go.

5. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.