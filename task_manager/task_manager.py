import re
import csv


class TasksManager:
    # A class for managing tasks of a list
    def __init__(self, list1=None):
        if list1 == None: # If no list is passed as parameter, it's set to empty
            self.tasks_list = []
        else:
            self.tasks_list = list1


    def prompt_new_task(self) -> str:
        # Prompts the user for a new task
        while True:
            task = input('Input a new task (only letters or "_"): ')
            if re.match(r'^[a-zA-Z_]+$', task):
                return task.lower()
            else:
                print('Incorrect name for the task. Try again!')


    def prompt_current_task(self) -> str:
        # Prompts the user for a task
        while True:
            task = input('Input current task: ')
            if re.match(r'^[a-zA-Z_]+$', task):
                return task.lower()
            else:
                print('Incorrect name for the task. Try again!')


    def print_tasks(self):
        # Print tasks as an enumerated column
        print('** TASKS **')
        for i, task in enumerate(self.tasks_list, start=1):
            print(f'{i}- {task.title()}')


    def add_task(self):
        # Get a task as parameter and adds it to the list
        new_task = self.prompt_new_task()
        if new_task not in self.tasks_list:
            self.tasks_list.append(new_task.lower())
        else:
            print('Task already exists')


    def remove_task(self):
        # Remove the task passed as parameter
        current_task = self.prompt_current_task()
        if current_task in self.tasks_list:
            self.tasks_list.remove(current_task)
        else:
            print('Task not in the list')


    def replace_task(self):
        # Replace an existing task by a new one
        current_task = self.prompt_current_task()
        if current_task in self.tasks_list:
            new_task = self.prompt_new_task()
            task_index = self.tasks_list.index(current_task)
            self.tasks_list[task_index] = new_task
        else:
            print('Task not in the list')


    def save_modifications(self):
        # Save tasks in a CSV file
        with open('tasks.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task'])  # Write the header
            writer.writerows([[task] for task in self.tasks_list])


    def load_tasks_from_csv(self):
        # Load tasks list forma a CSV file
        try:
            with open('tasks.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Omit the first row, which is the header
                self.tasks_list = [row[0] for row in reader]
        except FileNotFoundError:
            # If file doesn't exist, no action is performed
            pass
