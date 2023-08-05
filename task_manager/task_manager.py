import csv


class TasksManager:
    # A class for managing tasks of a list
    def __init__(self, list1=None):
        if list1 == None: # If no list is passed as parameter, it's set to empty
            self.tasks_list = []
        else:
            self.tasks_list = list1


    def add_task(self, new_task):
        # Get a task as parameter and adds it to the list
        self.tasks_list.append(new_task.lower())
     

    def remove_task(self, current_task):
        # Remove the task passed as parameter
        self.tasks_list.remove(current_task)
        self.save_modifications(self.tasks_list)


    def replace_task(self, current_task, new_task):
        # Replace an existing task by a new one
        task_index = self.tasks_list.index(current_task)
        self.tasks_list[task_index] = new_task


    def save_modifications(self, tasks_list):
        # Save tasks in a CSV file
        with open('tasks.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task'])  # Write the header
            writer.writerows([[task] for task in tasks_list])


    def load_tasks_from_csv(self):
        # Load tasks list forma a CSV file
        with open('tasks.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Omit the first row, which is the header
            self.tasks_list = [row[0] for row in reader]
            return self.tasks_list
     