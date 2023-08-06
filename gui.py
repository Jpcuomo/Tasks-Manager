from tkinter.messagebox import showinfo as alert
import customtkinter as ctk
from task_manager import TasksManager
import re
import os


class App(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Task Manager")
        #self.geometry("360x380")
        
        # Textboxes -------------------------------------------------------------------------------------------
        self.txt_new_task = ctk.CTkEntry(master=self, placeholder_text="Task to be added")
        self.txt_new_task.grid(row=2, column=2, padx=10, pady=20)

        self.txt_removed_task = ctk.CTkEntry(master=self, placeholder_text="Task to be removed")
        self.txt_removed_task.grid(row=3, column=2, padx=10, pady=20)
        
        self.txt_replaced_task = ctk.CTkEntry(master=self, placeholder_text="New task")
        self.txt_replaced_task.grid(row=5, column=3, padx=10, pady=20)
        
        self.txt_replacement_task = ctk.CTkEntry(master=self, placeholder_text="Task to be replaced")
        self.txt_replacement_task.grid(row=5, column=2, padx=10, pady=20)
        #------------------------------------------------------------------------------------------------------
        
        # Buttons ---------------------------------------------------------------------------------------------
        self.btn_load= ctk.CTkButton(master=self, text="Load file", command=self.btn_load_file_on_click)
        self.btn_load.grid(row=1, padx=10, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_add_task = ctk.CTkButton(master=self, text="Add task", command=self.btn_add_task_on_click)
        self.btn_add_task.grid(row=2, padx=10, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_remove = ctk.CTkButton(master=self, text="Remove task", command=self.btn_remove_on_click)
        self.btn_remove.grid(row=3, padx=10, pady=20, columnspan=2, sticky="nsew")

        self.btn_replace= ctk.CTkButton(master=self, text="Replace task", command=self.btn_replace_on_click)
        self.btn_replace.grid(row=5, padx=10, pady=20, columnspan=2, sticky="nsew")
        #-------------------------------------------------------------------------------------------------------
        
        self.t_m1 = TasksManager('tasks.csv')
        
        
        if os.path.exists(self.t_m1.file_name):
            self.btn_add_task.configure(state="disabled")
            self.btn_remove.configure(state="disabled")
            self.btn_replace.configure(state="disabled")
        else:
            self.btn_remove.configure(state="disabled")
            self.btn_replace.configure(state="disabled")
    
    
    def enable_buttons(self):
        self.btn_add_task.configure(state="enabled")
        self.btn_remove.configure(state="enabled")
        self.btn_replace.configure(state="enabled")


    def btn_load_file_on_click(self):
        # Loads the tasks already stored, if any, and displays'em in a window
        try:
            self.t_m1.tasks_list = self.t_m1.load_tasks_from_csv()
        except FileNotFoundError:
            message = 'File not found!\nAdd a task to create a file'
        else:
            if len(self.t_m1.tasks_list) != 0:
                message = "\n".join(f"- {task.title()}" for task in self.t_m1.tasks_list)
            else:
                message = 'Empty list'
        alert(title="Tasks:", message=message)
        
        # Buttons are enabled only if the CSV file exists
        # So, if it doesn't exists the user must add a task first to create the file
        if os.path.exists(self.t_m1.file_name):
            self.enable_buttons()
    
    
    def btn_add_task_on_click(self):
        # Add prompted task when pressed "add task" button
        new_task = self.txt_new_task.get()
        if new_task in self.t_m1.tasks_list:
            message = "This task already exists"
        elif new_task == '':
            message = "Add field can't be empty"
        elif re.match(r'^[a-zA-Z_]+$', new_task):
            self.t_m1.add_task(new_task)
            self.t_m1.save_modifications(self.t_m1.tasks_list)
            self.enable_buttons()
            message = f'"{new_task.title()}" was added to the list of tasks'
        else:
            message = "Task name incorrect!\nOnly admitted letters and _"
        alert(title="Add", message=message)
        self.txt_new_task.delete(0,100)
            
            
    def btn_remove_on_click(self):
        # Removes the task prompted in the field box
        current_task = self.txt_removed_task.get()
        if current_task in self.t_m1.tasks_list:
            self.t_m1.remove_task(current_task)
            message = f'"{current_task.title()}" was removed from the list'
            self.t_m1.save_modifications(self.t_m1.tasks_list)
        elif current_task == '':
            message = "Remove field can't be empty"
        else:
            message = f'"{current_task.title()}" doesn\'t exist'
        alert(title="Remove", message=message)        
        self.txt_removed_task.delete(0,100)
    
    
    def btn_replace_on_click(self):
        # Replace en axisting task by a new one entered by user
        current_task = self.txt_replacement_task.get()
        new_task = self.txt_replaced_task.get()
        if current_task in self.t_m1.tasks_list:
            if re.match(r'^[a-zA-Z_]+$', new_task):
                self.t_m1.replace_task(current_task, new_task)
                self.t_m1.save_modifications(self.t_m1.tasks_list)
                message = f'"{current_task.title()}" was replaced by "{new_task.title()}"'
            else:
                message = "Wrong task name"
        else:
            message = f"{current_task.title()} doesn't exit"
        alert(title="Replace", message=message)
        self.txt_replacement_task.delete(0,100)
        self.txt_replaced_task.delete(0,100)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()