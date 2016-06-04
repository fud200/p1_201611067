import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
import time
import math
import random
try:
    with open('save.txt','r') as f:
        for line in f:
            print line
except IOError as e:
    print e

t1.penup()
t1.goto(0,-300)
t1.goto(0,-250)
t1.write("start point")
stp=(0,-250)
t1.speed(50)
t1.shape("turtle")
wn.bgcolor("Black")
t1.pencolor("White")
t1.pendown()
def square(size,pos):
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    for i in range(4):
        t1.fd(size)
        t1.right(90)
def makeswirlSquare(size,bigger,sides,angle):
    t1.penup()
    t1.pencolor("Purple")
    t1.goto(-40,-60)
    t1.pendown()
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
        else:
            size=size
            t1.fd(size)
            t1.right(angle)
def save():
    played=open('save.txt', 'a')
    if score>=100:
        name = raw_input("Put your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\n'+'Score' + '\t'+ str(score) +'\t' + msg)
        played.write('\n' + 'Score' + '\t'+ str(score) +'\t' + msg)
        played.close()
        print("Click Screen")
	wn.exitonclick()
makeswirlSquare(10,5,20,90)
t1.fillcolor("Yellow")
t1.pencolor("White")
t1.begin_fill()
square(100,(-280,230))
t1.end_fill()
t1.fillcolor("Blue")
t1.begin_fill()
square(100,(180,230))
t1.end_fill()
t1.penup()
t1.goto(0,150)
t1.pendown
t1.fillcolor("Green")
t1.begin_fill()
t1.circle(50)
t1.end_fill()
t1.fillcolor("Red")
t1.begin_fill()
square(70,(40,0))
t1.end_fill()
t1.penup()
t1.pencolor("Red")
t1.goto(40,-80)
t1.write("Trap!!!!!")
t1.goto(-266,85)
t1.pencolor("Yellow")
t1.write("10 points")
t1.goto(-15,109)
t1.pencolor("Green")
t1.write("20 points")
t1.goto(174,104)
t1.pencolor("Blue")
t1.write("Quiz!!!!!!")
t1.goto(-53,-117)
t1.pencolor("Purple")
t1.write("Telleport")
t1.pencolor("Black")
t1.goto(stp)
print "welcome to my Game."
print "Your start point is 0, if your point >100, clear!!"
print "If you want to quit this game, press Q key"
x=float()
y=float()
score=0
def k1():
    global score
    (x,y)=t1.pos()
    t1.fd(20)
    if (-280<x<-180 and 130<y<230):
	score+=10
	print "Your score is %d " % score
	t1.goto(stp)
    if (180<x<280 and 130<y<230):
	"Quiz!!"
	t1.goto(stp)
	q=random.randrange(4)
	time.sleep(3)
	if q==0:
		sel1=raw_input("My birthday is on August Y or N:")
		if sel1=="Y":
			score=score+30
			print "Good"
		else:
			score=score-20
			print "...No..."
	if q==1:
		sel2=raw_input("I have a girlfirend Y or N:")
		if sel2=="Y":
			score=score+30
			print "Collect!"
		else:
			score=score-30
			print "No I have a girlfriend."
	if q==2:
		sel3=raw_input("I'm from Jeju Y or N:")
		if sel3=="Y":
			score=score+30
			print "Great!!"
		else:
			score=score-20
			print "That's NoNo"
	if q==3:
		sel4=raw_input("I have brother or sister Y or N:")
		if sel4=="N":
			score=score+30
			print "Good"
		else:
			score=score-20
			print "...No..."
		
	print "Your score is %d " % score
	t1.goto(stp)
    if (-68<x<-18 and -112<y<-52):
	print "teleport!!!!!!!!!!!!!!"
	a=random.randrange(-200,200)
	b=random.randrange(-200,200)
	t1.goto(a,b)
    if (40<x<110 and -70<y<0):
        t1.goto(stp)
	time.sleep(3)
	print "you fall in trap.. bye,bye."
	played=open('save.txt', 'a')
        name = raw_input("Put your name: ")
        msg='played {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\n'+'Score' + '\t'+ str(score) +'\t' + msg)
        played.write('\n' + 'Score' + '\t'+ str(score) +'\t' + msg)
        played.close()
	time.sleep(3)
	wn.bye()
    if (score<-40):
	print " you lose!"
	time.sleep(5)
	wn.bye()
    save()
    radius=50
    pos=(0,180)
    curpos=t1.pos()
    if math.sqrt(math.pow(curpos[0]-pos[0],2) + math.pow(curpos[1]-pos[1],2))<=radius:
	score+=20
	print "Your score is %d " % score
	t1.goto(stp)
def k2():
    t1.lt(30)
def k3():
    t1.right(30)
def k4():
    t1.bk(30)
def k5():
    wn.bye()
wn.onkey(k1,"Up")
wn.onkey(k2,"Left")
wn.onkey(k3,"Right")
wn.onkey(k4,"Down")
wn.onkey(k5,"q")
wn.listen()

turtle.mainloop()