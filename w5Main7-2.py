"""
@author khb
@since 160404
"""
"""
computes BMI
height:float
weight:float
"""
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def computerBMI():
	h1=raw_input("input your height: ")
	w1=raw_input("input your weight: ")
	height=float(h1)
	weight=float(w1)
	cm=height/100.
	bmi=weight/(cm*cm)
	if(bmi<18.5):
		print "low weight"
	elif(18.5<=bmi<25):
		print "normal weight"
	elif(25<=bmi<30):
    		print "ovesity"
	elif(30<=bmi):
		print "high obesity"
	else:
    		print "error"


def lab5():
	computerBMI()

def main():
	lab5()

main()

wn.exitonclick()