import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def mark_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        for index in selected_task_index:
            task_listbox.itemconfig(index, {'bg': 'light green'})

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("620x450")
root.resizable(0,0)
root.configure(bg="#00B2EE")

# Create the task entry and buttons using grid
task_entry = tk.Entry(root, width=50, font=18, background="#00688B")
task_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task",font=16, width=25, command=add_task, bg='#008B8B')
remove_button = tk.Button(root, text="Remove Task",font=16, width=25, command=remove_task, bg='#B22222')
done_button = tk.Button(root, text="Done", font=("Arial", 16), width=48, command=mark_done, bg="#008B00")

add_button.grid(row=1, column=0, padx=10, pady=10)
remove_button.grid(row=1, column=1, padx=10, pady=10)
done_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the task listbox using grid
task_listbox = tk.Listbox(root, width=50, bg="#00688B", font=14, selectmode=tk.MULTIPLE)
task_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
