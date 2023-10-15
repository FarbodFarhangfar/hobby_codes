import random
import tkinter as tk
from tkinter import messagebox

# Function to start the game with the chosen upper bound
def start_game():
    global secret_number, attempts, max_attempts, button_frame
    if button_frame:
        button_frame.destroy()  # Remove the previous number buttons
    upper_bound = int(upper_bound_var.get())
    secret_number = random.randint(1, upper_bound)
    attempts = 1
    max_attempts = 10  # Set maximum number of attempts to 10  for every game
    attempts = attempts - 1
    attempts_label.config(text=str(attempts))

    remaining_attempts_label.config(text=f"Attempts left: {max_attempts - attempts}")
    upper_bound_label.config(text=f"Upper Bound: {upper_bound}")
    upper_bound_option_menu.config(state="disabled")
    start_button.config(state="disabled")
    message_label.config(text="Guess the number (between 1 and " + str(upper_bound) + "):")
    entry.config(state="normal")
    check_button.config(state="normal")
    create_number_buttons(upper_bound)

# Function to check the guess
def check_guess(guess):
    global attempts
    try:
        if guess == secret_number:
            message = f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
            messagebox.showinfo("Guessing Game", message)

            start_game()  # Start the game over
        elif guess < secret_number:
            message = "Try a higher number."
        else:
            message = "Try a lower number"

        attempts += 1
        attempts_label.config(text=str(attempts))
        remaining_attempts_label.config(text=f"Attempts left: {max_attempts - attempts}")
        message_label.config(text=message)

        if attempts >= max_attempts:
            message = "Out of attempts. The number was " + str(secret_number)
            messagebox.showinfo("Guessing Game", message)
            start_game()  # Start the game over
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to create clickable number buttons organized in columns
def create_number_buttons(upper_bound):
    global button_frame
    button_frame = tk.Frame(root)
    button_frame.pack()

    buttons = []
    num_cols = get_num_columns(upper_bound)
    for num in range(1, upper_bound + 1):
        num_button = tk.Button(button_frame, text=str(num), command=lambda n=num: check_guess(n))
        buttons.append(num_button)

    for i, button in enumerate(buttons):
        row = i // num_cols
        col = i % num_cols
        button.grid(row=row, column=col, padx=5, pady=5)

# Function to determine the number of columns based on the upper bound
def get_num_columns(upper_bound):
    if upper_bound == 100:
        return 10
    elif upper_bound == 250:
        return 25
    elif upper_bound == 500:
        return 50
    else:
        return 1  # Default to one column

# Create the main window
root = tk.Tk()
root.title("Guessing Game")

# Create GUI components
upper_bound_label = tk.Label(root, text="Choose an upper bound:")
upper_bound_label.pack(pady=10)

options = [100, 250, 500]
upper_bound_var = tk.IntVar()
upper_bound_option_menu = tk.OptionMenu(root, upper_bound_var, *options)
upper_bound_option_menu.pack()

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

label = tk.Label(root, text="")
label.pack()

entry = tk.Entry(root, state="disabled")
entry.pack()

check_button = tk.Button(root, text="Check Guess", command=check_guess, state="disabled")
check_button.pack(pady=10)

attempts_label = tk.Label(root, text="")
attempts_label.pack()

remaining_attempts_label = tk.Label(root, text="")
remaining_attempts_label.pack()

button_frame = None  # Initialize button_frame

# Create a custom font style for "Try Higher" and "Try Lower" messages
bold_font = ("Helvetica", 12, "bold")

message_label = tk.Label(root, text="", font=bold_font)
message_label.pack(pady=10)

root.mainloop()
