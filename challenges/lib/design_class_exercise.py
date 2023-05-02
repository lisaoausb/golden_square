class TaskTracker():
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        self.name = name
        self.tasks = []
    # Parameters:
    #    name: string
    # Side effects:
    #   Sets the name property of the self object
        pass # No code here yet

    def add_task(self, task):
    # Parameters:
    #   task: string
    #   returns: nothing
        self.task = task
        self.tasks.append(task.lower())

    def see_tasks(self):
    # Parameters:
    #   None
    # returns: list of tasks
        tasks_formatted = ""
        if len(self.tasks) == 0:
            return "You're all caught up, Lisa."
        else:
            for task in self.tasks:
                if task != self.tasks[-1]:
                    tasks_formatted += task.lower() + ', '
                else: tasks_formatted += task.lower()
            return f"Your tasks: {tasks_formatted}"

    def mark_task_complete(self, task):
    # Parameters:
    #   task: string
    # returns: nothing
        self.task = task
        if len(self.tasks) == 0:
            raise Exception(f"Your list is empty, {self.name}.")
        elif task.lower() in self.tasks:
            self.tasks.remove(task.lower())
        else:
            raise Exception("No such task found. Check your spelling, Lisa, or see the list of tasks: sort out wardrobe, practise songs for wedding")