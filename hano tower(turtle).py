import turtle

turtle.setup(700, 700)
wn = turtle.Screen()
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t.speed("fastest")
t.pencolor("grey")
t.shapesize(1)
t.pensize(15)
t.penup()
t.setpos(-400, -100)
t.pendown()
t.setpos(400, -100)
t.setpos(400, -120)
t.setpos(-400, -120)
t.penup()
t.setpos(-200, -100)
t.pendown()
t.pensize(10)
t.forward(400)
t.left(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)

t.forward(200)
t.penup()
t.setpos(-200, -60)


def hidee(l, n):
    l.penup()
    t.shape("circle")


t1.shapesize(3)
t.fillcolor("black")
t1.fillcolor("blue")
t2.fillcolor("green")
t3.fillcolor("red")
t4.fillcolor("yellow")
t5.fillcolor("gray")

hidee(t, 3)
hidee(t1, 3)
hidee(t2, 3)
hidee(t3, 3)
hidee(t4, 3)
hidee(t5, 3)

t1.shape("circle")
t2.shape("circle")
t3.shape("circle")
t4.shape("circle")

t.shapesize(5)
t1.shapesize(4)
t2.shapesize(3)
t3.shapesize(2)
t4.shapesize(1.5)
aval = []
vasat = []
akhar = []
aval.append(-200)
vasat.append(0)
akhar.append(200)
aval.append(t)
aval.append(t1)
aval.append(t2)
aval.append(t3)
aval.append(t4)

n = -60
for i in range(1, len(aval)):
    aval[i].setpos(-200, n)
    n += 20


def h(n, a, b, c):
    if n == 1:
        a[-1].setpos(a[0], 220)
        if len(c) == 1:
            print("b")
            a[-1].setpos(c[0], -60)
        else:
            print("bb")
            i = len(c) - 1
            a[-1].setpos(c[0], -60 + (i * 20))
        b = a.pop()
        c.append(b)

    else:
        h(n - 1, a, c, b)
        a[-1].setpos(a[0], 220)
        if len(c) == 1:
            print("a")
            a[-1].setpos(c[0], -60)
        else:
            print("aa")
            i = len(c) - 1
            a[-1].setpos(c[0], -60 + (i * 20))
        c.append(a.pop())
        h(n - 1, b, a, c)


h(5, aval, vasat, akhar)

wn.mainloop()
