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
import datetime


def main():
    
    win = GraphWin("Smart Coffee Display",1365,900) 
    background_image="./static/26.gif"
    background(background_image, win)
    #cantor(600, 600, 60,win)
    #drawCircle(700,350,350,win)

    win.getMouse() # Pause to view result
    
    emailHeader("Email:", win)
    mail(win)

    win.getMouse() # Pause to view result

    newsHeader("News:", win)
    newsbox(win)
    news(win)
    
    win.getMouse() # Pause to view result

    eventsHeader("Events:",win)
    calendar(win)

    win.getMouse() # Pause to view result

    weatherHeader("Weather:", win)
    weather(win)

    win.getMouse() # Pause to view result

    time(win)


    # wait for mouse click to close window
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


def time(win):


	current_time = datetime.datetime.now().time()
	current_time = current_time.isoformat()

	t0= Text(Point(668, 50), current_time)
	t0.setFace('arial')
	t0.setStyle("bold")
	t0.setSize(30)
	t0.setTextColor("green")
	t0.draw(win)
	

def news(win):

	s = 1080
	font = "arial"
	n = getNews(5)

	t0= Text(Point(s, 100), n[0][0])
	t0.setFace(font)
	t0.setStyle("bold")
	t0.setSize(11)
	t0.setTextColor("black")
	t0.draw(win)

	t1= Text(Point(s, 120), n[0][1])
	t1.setFace(font)
	t1.setSize(10)
	t1.setTextColor("black")
	t1.draw(win)


	t2= Text(Point(s, 160), n[1][0])
	t2.setStyle("bold")
	t2.setFace(font)
	t2.setSize(11)
	t2.setTextColor("black")
	t2.draw(win)

	t3= Text(Point(s, 180), n[1][1])
	t3.setFace(font)
	t3.setSize(10)
	t3.setTextColor("black")
	t3.draw(win)

	t4= Text(Point(s, 220), n[2][0])
	t4.setStyle("bold")
	t4.setFace(font)
	t4.setSize(11)
	t4.setTextColor("black")
	t4.draw(win)

	t5= Text(Point(s, 240), n[2][1])
	t5.setFace(font)
	t5.setSize(10)
	t5.setTextColor("black")
	t5.draw(win)



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

	'''

	t16= Text(Point(s, 490), m[3][0])
	t16.setFace(font)
	t16.setSize(16)
	t16.setTextColor("white")
	t16.draw(win)

	t17= Text(Point(s, 510), m[3][1])
	t17.setFace(font)
	t17.setSize(16)
	t17.setTextColor("white")
	t17.draw(win)

	t18 = Text(Point(s, 530), m[3][2])
	t18.setFace(font)
	t18.setSize(16)
	t18.setTextColor("white")
	t18.draw(win)

	t19 = Text(Point(s, 550), m[3][3])
	t19.setFace(font)
	t19.setSize(16)
	t19.setTextColor("white")
	t19.draw(win)

	t20 = Text(Point(s, 570), m[3][4])
	t20.setFace(font)
	t20.setSize(16)
	t20.setTextColor("white")
	t20.draw(win)
'''


def weather(win):

	w = getWeather("03755")

	font = "arial"
	
	t0= Text(Point(307, 600), w[0][0])
	t0.setFace(font)
	t0.setStyle("bold italic")
	t0.setSize(28)
	t0.setTextColor("white")
	t0.draw(win)

	t1= Text(Point(305, 630), w[0][1])
	t1.setFace(font)
	t1.setStyle("bold italic")
	t1.setSize(28)
	t1.setTextColor("white")
	t1.draw(win)

	t3= Text(Point(470, 600), w[1][0])
	t3.setFace(font)
	t3.setStyle("bold italic")
	t3.setSize(28)
	t3.setTextColor("white")
	t3.draw(win)

	t4= Text(Point(470, 630), w[1][1])
	t4.setFace(font)
	t4.setStyle("bold italic")
	t4.setSize(28)
	t4.setTextColor("white")
	t4.draw(win)



def calendar(win):

	c = getCalendar(5)
	font = "arial"
	
	t0= Text(Point(1030, 520), c[0][0])
	t0.setFace(font)
	t0.setStyle("bold")
	t0.setSize(20)
	t0.setTextColor("white")
	t0.draw(win)

	t1= Text(Point(1030, 495), c[0][1])
	t1.setFace(font)
	t1.setStyle("bold")
	t1.setSize(20)
	t1.setTextColor("white")
	t1.draw(win)


	t2= Text(Point(1030, 585), c[1][0])
	t2.setFace(font)
	t2.setStyle("bold")
	t2.setSize(20)
	t2.setTextColor("white")
	t2.draw(win)

	t3= Text(Point(1030, 560), c[1][1])
	t3.setFace(font)
	t3.setStyle("bold")
	t3.setSize(20)
	t3.setTextColor("white")
	t3.draw(win)

	

def weatherHeader(tex, win):


	point = Point(330, 560)

	t = Text(point, tex)

	t.setSize(24)
	t.setStyle("bold")
	t.setFace("arial")

	t.setTextColor("yellow")

	t.draw(win)	

	

	point = Point(470, 660)

	t1 = Text(point, 'tomorrow')
    
	t1.setSize(16)
	t1.setStyle("bold")
	t1.setFace("arial")

	t1.setTextColor("yellow")

	t1.draw(win)	


	point = Point(307, 660)

	t2 = Text(point, 'today')
    
	
	t2.setSize(16)
	t2.setStyle("bold")
	t2.setFace("arial")

	t2.setTextColor("yellow")

	t2.draw(win)	



def emailHeader(tex, win):


	point = Point(130, 55)

	t = Text(point, tex)

	t.setSize(24)
	t.setStyle("bold")
	t.setFace("arial")

	t.setTextColor("yellow")

	t.draw(win)


def eventsHeader(tex, win):


	point = Point(925,470)

	t = Text(point, tex)

	t.setSize(24)
	t.setStyle("bold")
	t.setFace("arial")

	t.setTextColor("yellow")

	t.draw(win)


def newsHeader(tex, win):


	point = Point(895, 55)

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

	b = Rectangle(Point(860,75),Point(1300, 265))
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
