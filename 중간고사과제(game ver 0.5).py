import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import time
t1.penup()
t1.goto(0,-300)
t1.goto(0,-250)
t1.write("start point")
t1.speed(50)
t1.shape("turtle")
wn.bgcolor("Skyblue")
t1.fillcolor("pink")
t1.pendown()
def square(size,pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    for i in range(4):
        t1.fd(size)
        t1.right(90)
t1.penup()
t1.goto(0,270)
t1.write("if you reach square, you will get points")
stp=(0,-250)
t1.goto(stp)
square(50,(-200,200))
t1.penup()
t1.goto(-200,210)
t1.write("10 points")
square(30,(-20,230))
t1.penup()
t1.goto(-30,240)
t1.write("30 points")
square(10,(80,230))
t1.penup()
t1.goto(80,240)
t1.write("50ponts")
square(70,(-35,0))
t1.penup()
t1.pencolor("Red")
t1.goto(0,-80)
t1.write("Trap!!!!!")
t1.pencolor("Black")
t1.goto(stp)
print "welcome to my Game."
print "Your start point is 0, if your point >100, clear!!"
x=float()
y=float()
score=0
def k1():
    global score
    (x,y)=t1.pos()
    t1.fd(10)
    if (-200<x<-150 and 150<y<200):
	score+=10
	print "Your score is %d " % score
	t1.goto(stp)
    if (-20<x<10 and 200<y<230):
	score+=30
	print "Your score is %d " % score
	t1.goto(stp)
    if (80<x<90 and 220<y<230):
	score+=50
	print "Your score is %d " % score
	t1.goto(stp)
    if (-35<x<35 and -70<y<0):
	print "you fall in trap.. bye,bye."
	time.sleep(3)
	wn.bye()
    if (score>100):
	print " you win!"
	time.sleep(5)
	wn.bye()
def k2():
    t1.lt(30)
def k3():
    t1.right(30)
def k4():
    t1.bk(30)
wn.onkey(k1,"Up")
wn.onkey(k2,"Left")
wn.onkey(k3,"Right")
wn.onkey(k4,"Down")
wn.listen()

wn.exitonclick()