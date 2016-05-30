import os
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def getCoordsFromFile(aFile):
    fin=open(aFile,'r')
    mycoords=[]
    for line in fin:
        line1=line.split(',')
        aRect=[(line1[0],line1[1]),(line1[2],line1[3].strip())]
        mycoords.append(aRect)
    fin.close()
    return mycoords

def drawSquareWithCoords(coords):
	t1.penup()
	t1.goto(coords[0])
	t1.pendown()
	t1.goto(coords[1][0], coords[0][1])
	t1.goto(coords[1])
	t1.goto(coords[0][0], coords[1][1])
	t1.setpos(coords[0])
	
def lab13_6() :
	coords=getCoordsFromFile('coords.txt')
	drawSquareWithCoords(coords)

lab13_6()
wn.exitonclick()