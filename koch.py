import turtle
turtle.setup(700,700)
wn=turtle.Screen()
tt=turtle.Turtle()
tt.speed("fastest")
wn.tracer(0,0)
def poss(f):
    f.penup()
    f.setpos(0,200)
    f.pendown()
def f(t,size,order):
    if order == 1 :
        t.forward(size)
    else:
        f(t, size / 3, order - 1)
        t.left(60)
        f(t, size / 3, order - 1)
        t.right(120)
        f(t, size / 3, order - 1)
        t.left(60)
        f(t, size / 3, order - 1)
poss(tt)
tt.right(60)
"""
for i in range(3):
    f(tt, 400, 3)
    tt.right(120)
"""
for n in range(1):
    for i in range(3):
        f(tt, 400+(n*3), 5)
        tt.right(120)
    tt.penup()
    tt.setpos(0, 200+(n*3))
    tt.pendown()
tt.end_fill()
wn.mainloop()