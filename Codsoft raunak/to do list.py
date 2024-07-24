import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def update_task(self, task_id, new_task):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]["task"] = new_task

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks.pop(task_id)

    def complete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id]["completed"] = True

    def get_tasks(self):
        return self.tasks

class ToDoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.todo_list = ToDoList()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.todo_list.get_tasks()):
            task_text = task["task"]
            if task["completed"]:
                task_text += " (Completed)"
            self.task_listbox.insert(tk.END, f"{idx + 1}. {task_text}")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.todo_list.add_task(task)
            self.refresh_listbox()

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:")
            if new_task:
                self.todo_list.update_task(selected_index, new_task)
                self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.todo_list.delete_task(selected_index)
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.todo_list.complete_task(selected_index)
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Complete Task", "Please select a task to mark as completed.")

if _name_ == "_main_":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
