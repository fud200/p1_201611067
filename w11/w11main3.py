import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("mymaze.gif")
def k1():
    t1.fd(50)
wn.onkey(k1,"Up")
def k2():
    t1.lt(90)
def k3():
    t1.right(90)
def k4():
    t1.bk(50)
wn.onkey(k2,"Left")
wn.onkey(k3,"Right")
wn.onkey(k4,"Down")
wn.listen()
t1.penup()
t1.goto(-300,350)


wn.exitonclick()