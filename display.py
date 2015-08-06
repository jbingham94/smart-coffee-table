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
import textwrap


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
	stor_num = 5
	n = getNews(stor_num)
	effect_str = "bold"
	color_str = "black"
	big_sz = 11
	sm_sz = 10
	start_coord = 100
	sm_incr = 20
	mid_incr = 30
	big_incr = 40
	stories = 3
	elem = 3

	for x in range(0, stories):
		for y in range(0, elem):
			if y == elem-1:
				t = Text(Point(s, start_coord), textwrap.fill(n[x][y],80))
			else: 
				t = Text(Point(s, start_coord), n[x][y])
			t.setFace(font)
			if y == 0:
				t.setStyle(effect_str)
			t.setSize(big_sz)
			t.setTextColor(color_str)
			t.draw(win)
			if y == elem - 1: 
				start_coord = start_coord + big_incr
			elif y == elem - 2:
				start_coord = start_coord + mid_incr
			else:
				start_coord = start_coord + sm_incr

def mail(win):

	emails = 3
	m = getMail(emails)
	s = 270 # width for email text
	font = "arial"
	start_coord = 100
	sm_incr = 20
	mid_incr = 33
	big_incr = 37
	font_sz = 16
	color_str = "white"
	elem = 4

	for x in range(0, emails):
		for y in range(0, elem):
			t = Text(Point(s, start_coord), m[x][y])
			t.setFace(font)
			t.setSize(font_sz)
			t.setTextColor(color_str)
			t.draw(win)
			if y == elem-2: # second to last element in email
				start_coord = start_coord + big_incr
			elif y == elem-1: # last element in email
				start_coord = start_coord + mid_incr
			else: start_coord = start_coord + sm_incr


def weather(win):

	zipcode = "03755"
	font = "arial"
	style_str = "bold italic"
	color_str = "white"
	size = 28
	start_x_coord = 305
	start_y_coord = 600
	x_inc = 165
	y_inc = 30
	days = 2
	elem = 2
	w = getWeather(zipcode)

	for x in range(0, days):
		for y in range(0, elem):
			t = Text(Point(start_x_coord, start_y_coord), w[x][y])
			t.setFace(font)
			t.setStyle(style_str)
			t.setSize(size)
			t.setTextColor(color_str)
			t.draw(win)
			if y == elem-1:
				start_x_coord = start_x_coord + x_inc
				start_y_coord = start_y_coord - y_inc
			else:
				start_y_coord = start_y_coord + y_inc

def calendar(win):

	events = 2
	elem = 2
	c = getCalendar(events)
	font = "arial"
	style_str = "bold"
	size = 20
	color_str = "white"
	x_coord = 1030
	start_coord = 520
	decr = 25
	incr = 90
	no_more_events = 0

	for x in range(0, events):
		if no_more_events == 1:
			break
		for y in range(0, elem):
			if c[x][y] == 0:
				no_more_events = 1
				break
			t= Text(Point(x_coord, start_coord), c[x][y])
			t.setFace(font)
			t.setStyle(style_str)
			t.setSize(size)
			t.setTextColor(color_str)
			t.draw(win)
			if y == elem - 1:
				start_coord = start_coord + incr
			else:
				start_coord = start_coord - decr
	

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

	b = Rectangle(Point(860,75),Point(1300, 350))
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
