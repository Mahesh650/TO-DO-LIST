import tkinter as tk
from tkinter import messagebox, scrolledtext

# Store history
task_history = []

def add_task():
    title = title_entry.get()
    description = description_entry.get()
    deadline = deadline_entry.get()

    if title and description and deadline:
        messagebox.showinfo("Task Info", "Hello! WELCOME here is your task information.")
        task_info = f"Title: {title}\nDescription: {description}\nDeadline: {deadline}"
        listbox.insert(tk.END, task_info)
        task_history.append(task_info)

        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)

        update_history_display()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        del task_history[selected_index]
        update_history_display()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def clear_history():
    task_history.clear()
    listbox.delete(0, tk.END)
    update_history_display()

def update_history_display():
    history_display.delete("1.0", tk.END)
    if task_history:
        for idx, task in enumerate(task_history, 1):
            history_display.insert(tk.END, f"{idx}. {task}\n\n")
    else:
        history_display.insert(tk.END, "No task history yet.\n")

# GUI setup
root = tk.Tk()
root.title("To-Do List with History")
root.geometry("600x600")

# Labels and entry fields
tk.Label(root, text="Task Title:").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Description:").pack()
description_entry = tk.Entry(root, width=50)
description_entry.pack()

tk.Label(root, text="Deadline (e.g. 2025-07-01):").pack()
deadline_entry = tk.Entry(root, width=50)
deadline_entry.pack()

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Selected Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Clear All History", command=clear_history).pack(pady=5)

# Task Listbox
tk.Label(root, text="Current Tasks:").pack()
listbox = tk.Listbox(root, width=80, height=8)
listbox.pack()

# History section
tk.Label(root, text="Task History:").pack()
history_display = scrolledtext.ScrolledText(root, width=70, height=10, font=("Courier", 10))
history_display.pack()

update_history_display()

# Run app
root.mainloop()
