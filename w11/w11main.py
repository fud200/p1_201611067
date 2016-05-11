import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def line():
	t1.penup()
	t1.goto(-30,50)
	t1.pendown()
	t1.fd(60)
	t1.penup()
	t1.home()
def keyup():
	t1.fd(50)
	(a,b)=t1.pos()
	if (-30<a<30 and b==50):
		print "you trapped"
def keyback():
	t1.bk(50)
	(a,b)=t1.pos()
	if (-30<a<30 and b==50):
		print "you trapped"
def keyright():
	t1.rt(90)
def keyleft():
	t1.lt(90)
def mousegoto(x,y):
	t1.setpos(x,y)
	(a,b)=t1.pos()
	if (-30<a<30 and b==50):
		print "you trapped"
	
def end():
	wn.bye()
def addKeys():
	wn.onkey(keyup,"Up")
	wn.onkey(keyback,"Down")
	wn.onkey(keyright,"Right")
	wn.onkey(keyleft,"Left")
	wn.onkey(end,"q")
def addMouse():
	wn.onclick(mousegoto)


def lab11():
	line()
	addKeys()
	addMouse()
	wn.listen()
	turtle.mainloop()
lab11()