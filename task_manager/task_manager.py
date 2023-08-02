import re

class TasksManager:
    # A class for managing tasks of a list
    def __init__(self, list1=None):
        if list1 == None: # If no list is passed as parameter, it's set to empty
            self.tasks_list = []
        else:
            self.tasks_list = list1


    def prompt_task(self) -> str:
        # Prompts the user for a task
        while True:
            task = input('Input a desired task: ')
            if re.match(r'^[a-zA-Z_]+$', task):
                return task.lower()
            else:
                print('Incorrect name for the task. Try again!')


    def print_tasks(self):
        # Print tasks as an enumerated column
        print('** LIST OF TASKS **')
        for i, task in enumerate(self.tasks_list, start=1):
            print(f'{i}- {task.title()}')


    def add_task(self, new_task):
        # Get a task as parameter and adds it to the list
        self.tasks_list.append(new_task.lower())


    def del_task(self, task):
        # Remove the task passed as parameter
        if task in self.tasks_list:
            self.tasks_list.remove(task)


    def update_task(self, task, new_task):
        # Replace an existing task by a new one
        if task in self.tasks_list:
            task_index = self.tasks_list.index(task)
            self.tasks_list[task_index] = new_task


    def save_modificatios(self):
        pass
