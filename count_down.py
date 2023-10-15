import turtle as t
import time


# Function to draw the countdown timer
def draw_timer(timer_text):
    t.clear()

    # Draw the timer text
    t.penup()
    t.goto(0, 0)
    t.write(timer_text, align="center", font=("Arial", 30, "normal"))

    t.goto(0, -150)
    t.pendown()
    t.circle(150)


# Function to update the countdown timer
def update_timer(end_time):
    while True:
        current_time = time.time()
        remaining_time = max(0, end_time - current_time)

        hours = int(remaining_time / 3600)
        minutes = int((remaining_time % 3600) / 60)
        seconds = int(remaining_time % 60)
        tenths = int((remaining_time * 10) % 10)

        timer_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{tenths}"
        draw_timer(timer_text)

        if remaining_time <= 0:
            draw_timer("Time's up!")
            break

        t.update()
        time.sleep(0.1)


# Initialize Turtle
t.speed(0)
t.bgcolor("black")
t.color("white")
t.Screen().tracer(0)
t.hideturtle()
t.title("Countdown Timer")

# Set the countdown time (e.g., 1 hour, 5 minutes, 30 seconds)
countdown_hours = 1
countdown_minutes = 5
countdown_seconds = 30

end_time = time.time() + (countdown_hours * 3600) + (countdown_minutes * 60) + countdown_seconds

# Start the countdown
update_timer(end_time)

# Close the Turtle graphics window when clicked
t.exitonclick()
