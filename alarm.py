import tkinter as tk
from tkinter import messagebox
from time import strftime, sleep
from threading import Thread


def set_alarm():
    alarm_hour = int(entry_hour.get())
    alarm_minute = int(entry_minute.get())
    alarm_second = int(entry_second.get())

    try:
        if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59 or alarm_second < 0 or alarm_second > 59:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter valid hour, minute, and second values.")
        return

    alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}:{alarm_second:02d}"

    while True:
        current_time = strftime('%H:%M:%S')
        live_clock_label.config(text="Live Clock: " + current_time)
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time to wake up!")
            break
        root.update()
        sleep(1)


def update_live_clock():
    while True:
        current_time = strftime('%H:%M:%S')
        live_clock_label.config(text="Live Clock: " + current_time)
        root.update()
        sleep(1)


root = tk.Tk()
root.title("Alarm System")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

live_clock_label = tk.Label(frame, text="Live Clock: " + strftime('%H:%M:%S'))
live_clock_label.grid(row=0, column=0, columnspan=3)

label_hour = tk.Label(frame, text="Hour:")
label_hour.grid(row=1, column=0, sticky="w")

entry_hour = tk.Entry(frame)
entry_hour.grid(row=1, column=1)

label_minute = tk.Label(frame, text="Minute:")
label_minute.grid(row=2, column=0, sticky="w")

entry_minute = tk.Entry(frame)
entry_minute.grid(row=2, column=1)

label_second = tk.Label(frame, text="Second:")
label_second.grid(row=3, column=0, sticky="w")

entry_second = tk.Entry(frame)
entry_second.grid(row=3, column=1)

button_set_alarm = tk.Button(frame, text="Set Alarm", command=set_alarm)
button_set_alarm.grid(row=4, column=0, columnspan=3)

# Start a thread for the live clock
live_clock_thread = Thread(target=update_live_clock)
live_clock_thread.daemon = True
live_clock_thread.start()

root.mainloop()
