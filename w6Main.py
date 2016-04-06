import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def multiple():
	sum=0
	for i in range (0,1000):
		if not i%3 or i%5:
			sum=sum+i
	print sum
multiple()

wn.exitonclick()