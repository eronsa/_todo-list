import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List with Dark Mode")
root.geometry("400x500")

# Themes
light_theme = {
    "bg": "white",
    "fg": "black",
    "button_bg": "#f0f0f0",
    "listbox_bg": "white",
    "listbox_fg": "black"
}

dark_theme = {
    "bg": "#2e2e2e",
    "fg": "white",
    "button_bg": "#444444",
    "listbox_bg": "#3e3e3e",
    "listbox_fg": "white"
}

current_theme = light_theme

# Task storage
tasks = []

# Functions
def apply_theme():
    theme = current_theme
    root.config(bg=theme["bg"])
    task_entry.config(bg=theme["listbox_bg"], fg=theme["listbox_fg"])
    listbox.config(bg=theme["listbox_bg"], fg=theme["listbox_fg"])
    for widget in [add_button, done_button, delete_button, theme_button]:
        widget.config(bg=theme["button_bg"], fg=theme["fg"])

def toggle_theme():
    global current_theme
    current_theme = dark_theme if current_theme == light_theme else light_theme
    apply_theme()

def add_task():
    task_text = task_entry.get()
    if task_text != "":
        tasks.append({"text": task_text, "done": False})
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def toggle_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = not tasks[selected]["done"]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark done.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "[✔]" if task["done"] else "[ ]"
        listbox.insert(tk.END, f"{status} {task['text']}")

# UI Elements
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done / Undone", width=20, command=toggle_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack(pady=5)

theme_button = tk.Button(root, text="Toggle Light/Dark Mode", width=20, command=toggle_theme)
theme_button.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=20)

apply_theme()  # Apply initial theme

root.mainloop()