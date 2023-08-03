from task_manager import TasksManager


default_tasks = ['update', 'delete', 'random', 'insert', 'select', 'browse']

t_m1 = TasksManager(default_tasks)
t_m1.load_tasks_from_csv()
t_m1.print_tasks()
t_m1.replace_task()
t_m1.add_task()
t_m1.remove_task()
t_m1.print_tasks()
t_m1.save_modifications()
