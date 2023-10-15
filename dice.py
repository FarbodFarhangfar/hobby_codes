import turtle
import random


# Function to draw the dice
def draw_dice(x, y, value) -> None:
    # Move the turtle to the given coordinates
    draw_size = 100

    dice.color("red")
    dice.penup()
    dice.goto(x - draw_size / 2, y + draw_size / 2)
    dice.pendown()

    # Draw the dice outline
    dice.fillcolor("black")
    dice.begin_fill()
    for _ in range(4):
        dice.forward(draw_size)
        dice.right(90)
    dice.end_fill()

    # Draw the dots on the dice
    dice.penup()
    dice.goto(x, y)
    dice.pendown()
    dice.color("black")
    dice.pensize(3)

    dice.color("red")
    if value == 1:
        dice.dot(30)

    elif value == 2:
        dice.penup()
        dice.goto(x - draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x + draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(20)


    elif value == 3:
        dice.penup()
        dice.goto(x - draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x, y)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x + draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(20)

    elif value == 4:
        dice.penup()
        dice.goto(x - draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x + draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x - draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x + draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(20)

    elif value == 5:
        dice.penup()
        dice.goto(x - draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x - draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x, y)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x + draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(20)

        dice.penup()
        dice.goto(x + draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(20)

    elif value == 6:
        dice.penup()
        dice.goto(x - draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(15)

        dice.penup()
        dice.goto(x - draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(15)

        dice.penup()
        dice.goto(x - draw_size / 5, y)
        dice.pendown()
        dice.dot(15)

        dice.penup()
        dice.goto(x + draw_size / 5, y - draw_size / 5)
        dice.pendown()
        dice.dot(15)

        dice.penup()
        dice.goto(x + draw_size / 5, y)
        dice.pendown()
        dice.dot(15)

        dice.penup()
        dice.goto(x + draw_size / 5, y + draw_size / 5)
        dice.pendown()
        dice.dot(15)

    # Display the number
    dice.penup()
    dice.goto(x, y - draw_size)
    dice.pendown()
    dice.write(value, align="center", font=("Arial", 25, "bold"))


# Roll the dice and draw the result
def roll_dice() -> None:
    dice.clear()

    value = random.randint(1, 6)
    draw_dice(0, 0, value)


# Bind the roll_dice function to a key press event


if __name__ == '__main__':
    # Setup the turtle screen
    screen = turtle.Screen()
    screen.title("Dice")
    screen.bgcolor("white")

    # Create the turtle object
    dice = turtle.Turtle()
    dice.speed(0)
    dice.hideturtle()

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()

    pen.penup()
    pen.goto(0, 0 + 200)
    pen.pendown()
    pen.write("press space to roll the dice", align="center", font=("Arial", 25, "bold"))

    screen.onkeypress(roll_dice, "space")
    screen.listen()

    # Start the main event loop
    turtle.mainloop()
