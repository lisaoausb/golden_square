from lib.todo import Todo 
# the above is needed for pytest

# from class_system_todo import Todo
# the above here is what we use for the debugger (file is in same
# directory)

class TodoList:
    def __init__(self):
        self._to_do_list = []
        # self.incomplete_tasks_list = []
        # self.completed_tasks = []
    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._to_do_list.append(todo)
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        self.incomplete_tasks_list = []
        for task in self._to_do_list:
            if task.complete == False:
                self.incomplete_tasks_list.append(task)
        return self.incomplete_tasks_list
    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        completed_tasks = []
        for task in self._to_do_list:
            if task.complete == True:
                completed_tasks.append(task)
        return completed_tasks
    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self._to_do_list:
            task.mark_complete()
        self.incomplete_tasks_list = []