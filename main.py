import tkinter as tk


def add_tasks():
    task = entry.get()
    if task:
        tasks.append(task)
        updatetask_display()
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = display_tasks.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        updatetask_display()

def updatetask_display():
    # Clear the existing tasks display
    display_tasks.delete(0, tk.END)

    # Insert each task into the tasks display
    for task in tasks:
        display_tasks.insert(tk.END, task)

def sort_tasks():
    global tasks
    tasks.sort()
    updatetask_display()
# Create the main window or root widget
root = tk.Tk()

# Customize the root widget (optional)
root.title("To do list")
root.geometry("700x600")  # Set the initial size of the window


heading_label=tk.Label(root, text="My Tasks" , font=("Roboto" ,15 , 'bold'), bg='#666699',fg='white', width=2000)
heading_label.pack(pady=10)

# Add other widgets or functionality to the root widget
tasks = []


entry = tk.Entry(root, width=40 , font=("Roboto" ,12))
entry.pack(pady=10 , ipady=20)

add_button = tk.Button(root, text="Add Task", command=add_tasks , bg="#666699" , fg="white")
add_button.pack()

frame = tk.Frame(root)
frame.pack(pady=10 )

# Add a scrollbar to the Listbox
display_tasks = tk.Listbox(frame, height=25, width=70)
display_tasks.pack(side="left")
scrollbar = tk.Scrollbar(frame, orient="vertical")
scrollbar.config(command=display_tasks.yview)
scrollbar.pack(side="right", fill="y")

display_tasks.config(yscrollcommand=scrollbar.set)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#666699" , fg="white")
delete_button.pack()

sort_button = tk.Button(root, text="Sort Tasks", command=sort_tasks, bg="#666699", fg="white")
sort_button.pack()

# Start the Tkinter event loop
root.mainloop()
