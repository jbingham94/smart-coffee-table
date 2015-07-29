# display.py
#
# Authors: Chris Livingston and Jasper Bingham
#
# Made for CS 69 Project: Smart Coffee Table 
#
# This module drives the graphics for the displays
# associated with the functionality of the module 
# smartCoffeeTable.py
#
# The main method of this module can be changed and called from the raspberry pi GPIO module
#


from graphics import *
from smartCoffeeTable import *


def main():
    
    win = GraphWin("Smart Coffee Display",1365,900) 
    background_image="./static/26.gif"
    background(background_image, win)
    #cantor(600, 600, 60,win)
    #drawCircle(700,350,350,win)

    
    emailHeader("Email:", win)
    mail(win)
    newsbox(win)
    news(win)


    # wait for mouse click to close window
    win.getMouse() # Pause to view result
    win.close()    # Close window when done



def news(win):

	s = 1200
	font = "helvetica"
	n = getNews(5)

	t0= Text(Point(s, 100), n[0][0])
	t0.setFace(font)
	t0.setSize(14)
	t0.setTextColor("black")
	t0.draw(win)

	t1= Text(Point(s, 120), n[0][1])
	t1.setFace(font)
	t1.setSize(14)
	t1.setTextColor("black")
	t1.draw(win)





def mail(win):

	m = getMail(5)
	s = 270 # width for email text
	font = "arial"

	t0= Text(Point(s, 100), m[0][0])
	t0.setFace(font)
	t0.setSize(16)
	t0.setTextColor("white")
	t0.draw(win)

	t1= Text(Point(s, 120), m[0][1])
	t1.setFace(font)
	t1.setSize(16)
	t1.setTextColor("white")
	t1.draw(win)

	t3 = Text(Point(s, 140), m[0][2])
	t3.setFace(font)
	t3.setSize(16)
	t3.setTextColor("white")
	t3.draw(win)

	t4 = Text(Point(s, 160), m[0][3])
	t4.setFace(font)
	t4.setSize(16)
	t4.setTextColor("white")
	t4.draw(win)

	t5 = Text(Point(s, 197), m[0][4])
	t5.setFace(font)
	t5.setSize(16)
	t5.setTextColor("white")
	t5.draw(win)


	
	t6= Text(Point(s, 230), m[1][0])
	t6.setFace(font)
	t6.setSize(16)
	t6.setTextColor("white")
	t6.draw(win)

	t7= Text(Point(s, 250), m[1][1])
	t7.setFace(font)
	t7.setSize(16)
	t7.setTextColor("white")
	t7.draw(win)

	t8 = Text(Point(s, 270), m[1][2])
	t8.setFace(font)
	t8.setSize(16)
	t8.setTextColor("white")
	t8.draw(win)

	t9 = Text(Point(s, 290), m[1][3])
	t9.setFace(font)
	t9.setSize(16)
	t9.setTextColor("white")
	t9.draw(win)

	t10 = Text(Point(s, 327), m[1][4])
	t10.setFace(font)
	t10.setSize(16)
	t10.setTextColor("white")
	t10.draw(win)

	t11= Text(Point(s, 360), m[2][0])
	t11.setFace(font)
	t11.setSize(16)
	t11.setTextColor("white")
	t11.draw(win)

	t12= Text(Point(s, 380), m[2][1])
	t12.setFace(font)
	t12.setSize(16)
	t12.setTextColor("white")
	t12.draw(win)

	t13 = Text(Point(s, 400), m[2][2])
	t13.setFace(font)
	t13.setSize(16)
	t13.setTextColor("white")
	t13.draw(win)

	t14 = Text(Point(s, 420), m[2][3])
	t14.setFace(font)
	t14.setSize(16)
	t14.setTextColor("white")
	t14.draw(win)

	t15 = Text(Point(s, 457), m[2][4])
	t15.setFace(font)
	t15.setSize(16)
	t15.setTextColor("white")
	t15.draw(win)


def emailHeader(tex, win):


	point = Point(130, 75)

	t = Text(point, tex)

	t.setSize(24)
	t.setStyle("bold")
	t.setFace("arial")

	t.setTextColor("yellow")

	t.draw(win)


def background(img_name, win):

	#create a point by specifying the x and y positions
	point1 = Point(680, 350) 
	# create image object
	image1 = Image(point1, img_name)
	#make it show up in the window
	image1.draw(win)


def newsbox(win):

	b = Rectangle(Point(900,80),Point(1270, 275))
	b.setFill("white")
	b.draw(win)




def drawCircle(x,y,radius,win):
	c = Circle(Point(x,y), radius)
	c.draw(win)

	if (radius > 25):
		
		drawCircle(x+radius/2,y, radius/2,win)
		drawCircle(x-radius/2,y, radius/2,win)
		drawCircle(x,y+radius/2,radius/2,win)
		drawCircle(x,y-radius/2,radius/2,win)
def cantor(x,y,len,win):

	if (len>=1): 
		l = Line(Point(x,y),Point(x+len,y))
		l.draw(win)
 
	  	y += 20
 
  		cantor(x,y,len/3,win)
  		cantor(x+len*2/3,y,len/3,win)



main()
