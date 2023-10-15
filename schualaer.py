import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime
from tkcalendar import Calendar

# Function for displaying a message box
def show_message(task_name):
    messagebox.showinfo("Task Notification", f"{task_name} is scheduled to run now!")

# Function to schedule a recurring task with a specified interval
def schedule_recurring_task(task_name, interval_seconds, set_button, stop_button):
    def repeated_task():
        while not stop_flag[0]:
            show_message(task_name)
            time.sleep(interval_seconds)

    stop_flag[0] = False
    threading.Thread(target=repeated_task, daemon=True).start()
    set_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Function to schedule a one-time task at a specified date and time
def schedule_one_time_task(task_name, selected_date, time_str, set_button, stop_button):
    try:
        current_date = datetime.now().strftime("%Y-%m-%d")
        scheduled_datetime = datetime.strptime(f"{current_date} {time_str}", "%Y-%m-%d %H:%M")
        current_datetime = datetime.now()

        if scheduled_datetime > current_datetime:
            delta = scheduled_datetime - current_datetime
            seconds_delay = delta.total_seconds()
            threading.Timer(seconds_delay, show_message, args=(task_name,)).start()
            set_button.config(state=tk.DISABLED)
            stop_button.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Invalid Schedule", "The selected time has already passed.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid time format (HH:MM).")

# Function to stop a task
def stop_task(task_name, set_button, stop_button):
    stop_flag[0] = True
    set_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("Task Scheduler")

# Task 1: Recurring Task
label_task1_interval = tk.Label(root, text="Task 1 - Enter Interval (seconds):")
label_task1_interval.grid(row=0, column=0)
entry_task1_interval = tk.Entry(root)
entry_task1_interval.grid(row=0, column=1)
button_set_task1 = tk.Button(root, text="Set Recurring Task", command=lambda: schedule_recurring_task("Recurring Task", int(entry_task1_interval.get()), button_set_task1, button_stop_task1))
button_set_task1.grid(row=0, column=2)
button_stop_task1 = tk.Button(root, text="Stop Recurring Task", state=tk.DISABLED, command=lambda: stop_task("Recurring Task", button_set_task1, button_stop_task1))
button_stop_task1.grid(row=0, column=3)

# Add a line separator between the two cases
separator = tk.Label(root, text="----------------------")
separator.grid(row=1, column=0, columnspan=4)

# Task 2: One-time Task
label_task2_date = tk.Label(root, text="Task 2 - Select Date:")
label_task2_date.grid(row=2, column=0)
calendar_task2 = Calendar(root)
calendar_task2.grid(row=2, column=1)
label_task2_time = tk.Label(root, text="Enter Time (HH:MM):")
label_task2_time.grid(row=3, column=0)
entry_task2_time = tk.Entry(root)
entry_task2_time.grid(row=3, column=1)
button_set_task2 = tk.Button(root, text="Set One-time Task", command=lambda: schedule_one_time_task("One-time Task", calendar_task2.get_date(), entry_task2_time.get(), button_set_task2, button_stop_task2))
button_set_task2.grid(row=3, column=2)
button_stop_task2 = tk.Button(root, text="Stop One-time Task", state=tk.DISABLED, command=lambda: stop_task("One-time Task", button_set_task2, button_stop_task2))
button_stop_task2.grid(row=3, column=3)

# Create a stop flag for tasks
stop_flag = [False]

# Start tkinter main loop
root.mainloop()
