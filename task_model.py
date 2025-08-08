class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.is_completd = False    

    def get_task_name(self):
        return self.task_name    

    def set_done(self):
        self.is_done = True

    def remove_task(self):
        self.task_name = None
        self.is_done = False    

    def is_done(self):
        return self.is_done

    def mark_as_complete(self):
        self.is_completd = True

    def is_completd(self):
        return self.is_completd
         

