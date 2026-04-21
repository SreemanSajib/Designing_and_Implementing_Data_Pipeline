# main.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

# -----------------------
# Login function
# -----------------------
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to database and check credentials
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        # Show success message in GUI
        messagebox.showinfo("Success", f"Welcome, {username}!")
        open_task_window(user[0])  # Pass user_id to task window
    else:
        messagebox.showerror("Error", "Wrong username or password")

# -----------------------
# Task window function
# -----------------------
def open_task_window(user_id):
    task_window = tk.Toplevel()
    task_window.title("Tasks")
    task_window.geometry("450x400")

    # Label for task list
    tk.Label(task_window, text="Your Tasks").pack(pady=5)

    # Entry to add new task
    entry_new_task = tk.Entry(task_window, width=35)
    entry_new_task.pack(pady=5)

    # Entry to edit selected task
    entry_edit_task = tk.Entry(task_window, width=35)
    entry_edit_task.pack(pady=5)

    # Listbox to display tasks
    listbox_tasks = tk.Listbox(task_window, width=50)
    listbox_tasks.pack(pady=5)

    # -----------------------
    # Functions for task buttons
    # -----------------------
    def load_tasks():
        """Load all tasks of this user from database"""
        listbox_tasks.delete(0, tk.END)
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("SELECT task FROM tasks WHERE user_id=?", (user_id,))
        tasks = cursor.fetchall()
        conn.close()
        for t in tasks:
            listbox_tasks.insert(tk.END, t[0])

    def add_task():
        """Add new task to database"""
        task_text = entry_new_task.get()
        if task_text == "":
            return
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task_text))
        conn.commit()
        conn.close()
        entry_new_task.delete(0, tk.END)
        load_tasks()

    def delete_task():
        """Delete selected task from database"""
        selected_task = listbox_tasks.get(tk.ACTIVE)
        if selected_task == "":
            return
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE user_id=? AND task=?", (user_id, selected_task))
        conn.commit()
        conn.close()
        load_tasks()

    def edit_task():
        """Edit selected task and update database"""
        selected_task = listbox_tasks.get(tk.ACTIVE)
        new_task = entry_edit_task.get()
        if selected_task == "" or new_task == "":
            return
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET task=? WHERE user_id=? AND task=?", (new_task, user_id, selected_task))
        conn.commit()
        conn.close()
        entry_edit_task.delete(0, tk.END)
        load_tasks()

    # -----------------------
    # Bind listbox selection to auto-fill edit entry
    # -----------------------
    def on_select(event):
        selected_task = listbox_tasks.get(tk.ACTIVE)
        entry_edit_task.delete(0, tk.END)
        entry_edit_task.insert(0, selected_task)

    listbox_tasks.bind("<<ListboxSelect>>", on_select)

    # -----------------------
    # Buttons for tasks
    # -----------------------
    tk.Button(task_window, text="Add Task", width=15, command=add_task).pack(pady=5)
    tk.Button(task_window, text="Delete Task", width=15, command=delete_task).pack(pady=5)
    tk.Button(task_window, text="Update Task", width=15, command=edit_task).pack(pady=5)

    # Load tasks on window open
    load_tasks()

# -----------------------
# Main login window
# -----------------------
root = tk.Tk()
root.title("Login")
root.geometry("350x200")

tk.Label(root, text="Username").pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

tk.Button(root, text="Login", width=15, command=login).pack(pady=10)

root.mainloop()