from lib.class_system_todo import Todo 
# the above is needed for pytest

# from class_system_todo import Todo
# the above here is what we use for the debugger (file is in same
# directory)

class TodoList:
    def __init__(self):
        self._incompletes = []
        self._completes = []

    def add(self, todo):
        self._incompletes.append(todo)
      
    def incomplete(self):
        if self._incompletes == []:
            raise Exception('No outstanding tasks')
        else:
            return self._incompletes

    def complete(self):
        self._completes = [todo for todo in self._incompletes if todo.completed == True]
        self._incompletes = [todo for todo in self._incompletes if todo.completed == False]
        # for todo in self._incompletes:
        #     if todo.completed == True:
        #         self._completes.append(todo)
        #         self._incompletes.remove(todo)
        if self._completes == []:
            raise Exception('No tasks completed yet')
        else:
            return self._completes
        # Returns:
        #   A list of Todo instances representing the todos that are complete

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self._incompletes:
            todo.mark_complete()
        self._completes = self._completes + [todo for todo in self._incompletes if todo.completed == True]
        self._incompletes = [todo for todo in self._incompletes if todo.completed == False]