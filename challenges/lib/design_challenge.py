def track_tasks(task):
    if task != "":
        return '#TODO' in task
    else: raise Exception('No task given.')