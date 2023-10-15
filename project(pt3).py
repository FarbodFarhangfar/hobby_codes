import turtle
import time

turtle.setup(700, 700)
wn = turtle.Screen()
wn.title("turtle becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(10)
tess2 = turtle.Turtle()
tess3 = turtle.Turtle()
tess2.speed(1000)
tess3.speed(1000)


def draw_housing():
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


def draw_leg():
    tess.begin_fill()
    tess.forward(30)
    tess.right(90)
    tess.forward(50)

    tess.right(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(50)
    tess.right(90)

    tess.forward(210)
    tess.left(90)
    tess.forward(20)
    tess.left(90)

    tess.forward(210)

    tess.right(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(50)
    tess.left(90)
    tess.forward(50)
    tess.right(90)

    tess.forward(50)
    tess.left(90)
    tess.forward(50)
    tess.left(180)
    tess.end_fill()


draw_housing()
draw_leg()


def draw_circle(t, n):
    t.penup()
    t.forward(40)
    t.left(90)
    t.forward((n * 70) + 50)
    t.shape("circle")
    t.shapesize(3)
    t.fillcolor("grey")


draw_circle(tess, 0)
draw_circle(tess2, 1)
draw_circle(tess3, 2)
state_num = 0


def advance_state_machine():
    tess.fillcolor("grey")
    tess2.fillcolor("grey")
    tess3.fillcolor("grey")
    global state_num
    if state_num == 0:
        tess.fillcolor("green")
        state_num = 1
        # wn.ontimer(advance_state_machine, 3000)
        countdown(4)
        advance_state_machine()


    elif state_num == 1:
        tess.fillcolor("green")
        tess2.fillcolor("orange")
        state_num = 2
        # wn.ontimer(advance_state_machine, 1000)

        countdown(1)
        advance_state_machine()

    elif state_num == 2:
        tess2.fillcolor("orange")
        state_num = 3
        # wn.ontimer(advance_state_machine, 1000)

        countdown(1)
        advance_state_machine()

    else:
        tess3.fillcolor("red")
        state_num = 0
        # wn.ontimer(advance_state_machine, 2000)

        countdown(4)
        advance_state_machine()


countdown_turtle = turtle.Turtle()
countdown_turtle.speed(0)
countdown_turtle.penup()
countdown_turtle.hideturtle()
countdown_turtle.goto(0, 0)
countdown_turtle.forward(45)
countdown_turtle.right(90)
countdown_turtle.forward(95)


# Function to display the countdown
def countdown(seconds):
    seconds = seconds*10
    for i in range(seconds, 0, -1):
        centiseconds = i % 10
        countdown_turtle.clear()
        countdown_turtle.write(f"{i // 10}.{centiseconds:01}", align="center",
                               font=("Arial", 26, "normal"))
        time.sleep(0.1)

    countdown_turtle.clear()


# Set the countdown duration (in seconds)






advance_state_machine()
wn.mainloop()
