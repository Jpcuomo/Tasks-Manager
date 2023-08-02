from task_manager import TasksManager


default_tasks = ['update', 'delete', 'random', 'insert', 'select', 'browse']

t_m1 = TasksManager(default_tasks)
new_task = t_m1.prompt_task()
aux_task = 'delete'

t_m1.update_task(aux_task, new_task)
t_m1.print_tasks()
