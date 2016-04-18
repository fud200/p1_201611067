import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
d=dict()
d=({0:(0,0),1:(70,0),2:(70,70),3:(0,70),4:(0,0)})
def lab7_3():
	for i in range (1,5):
		t1.goto(d[i])
	for h in range (1,5):
		print d[h]
	wn.exitonclick()

def main():
	lab7_3()

if __name__=="__main__":
	main()
