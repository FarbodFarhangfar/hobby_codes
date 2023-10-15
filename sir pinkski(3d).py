import turtle

turtle.setup(700, 700)
wn = turtle.Screen()
wn.tracer(0, 0)
tt = turtle.Turtle()
tt2 = turtle.Turtle()
tt.speed(100)
tt2.speed(100)
tt.penup()
tt2.penup()
tt.setpos(-200, -200)
tt2.setpos(-200, -200)
tt.pendown()
tt2.pendown()
n = 0


def f(t, size, order):
    if order == 1:
        t.forward(size)
        t.left(120)
        t.forward(size)
        t.left(120)
        t.forward(size)
    else:
        if order == 4:
            t.fillcolor("green")
        t.begin_fill()
        f(t, size / 2, order - 1)
        t.end_fill()
        t.left(120)
        t.forward(size / 2)
        if order == 4:
            t.fillcolor("blue")
        t.begin_fill()
        f(t, size / 2, order - 1)
        t.end_fill()
        t.right(120)
        t.forward(size / 2)
        t.right(120)
        if order == 4:
            t.fillcolor("black")
        t.begin_fill()
        f(t, size / 2, order - 1)
        t.end_fill()
        t.forward(size / 2)


f(tt, 400, 5)
tt2.forward(400)
tt2.left(70)


def f2(t, size, size2, size3, order):
    if order == 1:
        t.forward(size)
        t.left(79)
        t.forward(size2)
        t.left(151)
        t.forward(size3)
        t.left(130)
    else:
        if order == 4:
            t.fillcolor("darkblue")
        t.begin_fill()
        f2(t, size / 2, size2 / 2, size3 / 2, order - 1)
        t.end_fill()
        t.left(50)
        t.forward(size3 / 2)
        t.right(50)
        if order == 4:
            t.fillcolor("gray")
        t.begin_fill()
        f2(t, size / 2, size2 / 2, size3 / 2, order - 1)
        t.end_fill()
        t.right(101)
        t.forward(size2 / 2)
        t.left(101)
        if order == 4:
            t.fillcolor("darkgreen")
        t.begin_fill()
        f2(t, size / 2, size2 / 2, size3 / 2, order - 1)
        t.end_fill()
        t.right(180)
        t.forward(size / 2)
        t.right(180)


f2(tt2, 198, 313, 400, 5)
tt2.hideturtle()
tt.hideturtle()
wn.mainloop()
