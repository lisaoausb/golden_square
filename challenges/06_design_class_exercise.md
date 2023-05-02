TASKS 06_exercise Class Design Recipe

1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

class TaskTracker:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
    # Parameters:
    #    name: string
    # Side effects:
    #   Sets the name property of the self object
    pass # No code here yet

    def add_task(self, task):
    # Parameters:
    #   task: string
    #   returns: nothing

    def see_tasks(self):
    # Parameters:
    #   None
    # returns: list of tasks

    def mark_task_complete(self, task):
    # Parameters:
    #   task: string
    # returns: nothing

# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

def see_list_of_two_tasks():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    task_list = tracker.see_tasks()
    assert task_list == 'Your tasks: sort out wardrobe, practise songs for wedding'

def see_list_of_one_task_after_completing_another():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    tracker.mark_task_complete('Practise songs for wedding')
    assert task_list == 'Your tasks: sort out wardrobe'

def see_list_of_one_task_after_completing_another():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    tracker.mark_task_complete('practise songs for wedding')
    assert task_list == 'Your tasks: sort out wardrobe'

def see_list_but_no_tasks():
    tracker = TaskTracker('Lisa')
    task_list = tracker.see_tasks()
    assert task_list == 'You're all caught up, Lisa.'

def mark_misspelt_or_nonexisting_task_complete_on_nonempty_list():
    tracker = TaskTracker('Lisa')
    tracker.add_task('Sort out wardrobe')
    tracker.add_task('Practise songs for wedding')
    with pytest.raises(Exception) as e:
        tracker.mark_task_complete('Practice songs for wedding')
    error = str(e.value)
    assert error == 'No such task found. Check your spelling, Lisa, or see the list of tasks: sort out wardrobe, practise songs for wedding'

def mark_task_complete_on_empty_list():
    tracker = TaskTracker('Lisa')
    with pytest.raises(Exception) as e:
        tracker.mark_task_complete('Practice songs for wedding')
    error = str(e.value)
    assert error == 'Your list is empty, Lisa.'



# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
Encode each example as a test. You can add to the above list as you go.

4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.