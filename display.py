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
import time
from dateutil.relativedelta import relativedelta
import textwrap


def main():

    # make window
    win = GraphWin("Smart Coffee Display",1365,900) 

    # set up background
    background_image="./static/26.gif"
    background(background_image, win)

    # set up main modules
    mail(win)
    news(win)
    calendar(win)
    weather(win)

	# create continuous loop to make running clock
    var = 1
    while var == 1: 
    	obj = clock(win)
    	time.sleep(1)
    	obj.undraw()

    # wait for mouse click to close window
    click = win.getMouse() # Pause to view result
    print click.getX()
    print click.getY()
    win.close()    # Close window when done


def clock(win):

	# displaying time
	time = datetime.datetime.now().time()
	time_str = time.strftime('%l:%M:%S %p')
	t= Text(Point(668, 50), time_str)
	t.setFace('arial')
	t.setStyle("bold")
	t.setSize(30)
	t.setTextColor("green")
	t.draw(win)
	return t

def news(win):

	# variables
	font = "arial"
	effect_str = "bold"
	color_str = "white"
	header_color_str = "yellow"
	header_str = "NEWS"
	s = 1095
	stor_num = 5
	big_sz = 11
	sm_sz = 10
	start_coord = 100
	sm_incr = 20
	mid_incr = 30
	big_incr = 40
	stories = 3
	elem = 3
	header_x = 1095
	header_y = 50
	header_sz = 24
	n = getNews(stor_num)

	# header stuff
	point = Point(header_x, header_y)
	t = Text(point, header_str)
	t.setSize(header_sz)
	t.setStyle(effect_str)
	t.setFace(font)
	t.setTextColor(header_color_str)
	t.draw(win)

	# stories

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

	# variables
	header_style = "bold"
	header_text = "EMAIL"
	header_color_str = "yellow"
	font = "arial"
	color_str = "white"
	emails = 3
	x_coord = 270 # width for email text
	header_x = 270
	header_y = 50
	header_size = 24
	start_coord = 100
	sm_incr = 20
	mid_incr = 33
	big_incr = 35
	font_sz = 14
	elem = 4
	subj_slot = 2
	m = getMail(emails)

	# header stuff
	point = Point(header_x, header_y)
	t = Text(point, header_text)
	t.setSize(header_size)
	t.setStyle(header_style)
	t.setFace(font)
	t.setTextColor(header_color_str)
	t.draw(win)

	# displaying emails
	for x in range(0, emails):
		for y in range(0, elem):
			t = Text(Point(x_coord, start_coord), m[x][y])
			t.setFace(font)
			t.setSize(font_sz)
			t.setTextColor(color_str)
			if y == subj_slot:
				t.setStyle(header_style)
			t.draw(win)
			if y == elem-2: # second to last element in email
				start_coord = start_coord + big_incr
			elif y == elem-1: # last element in email
				start_coord = start_coord + mid_incr
			else: start_coord = start_coord + sm_incr


def weather(win):

	zipcode = "03755"
	font = "arial"
	style_str = "bold"
	color_str = "white"
	tag_color_str = "yellow"
	header_str = "WEATHER"
	size = 20
	start_x_coord = 170
	start_y_coord = 500
	x_coord = start_x_coord
	y_coord = start_y_coord
	bottom_x_coord = 270
	x_inc = 200
	y_inc = 30
	newline_y_inc = 100
	days = 5
	elem = 2
	w = getWeather(zipcode)
	style_str = "bold"
	font = "arial"
	header_sz = 24
	day_sz = 16
	# for header
	header_x = 270
	header_y = 450
	incr = 200

	# header setup
	point = Point(header_x, header_y)
	t = Text(point, header_str)
	t.setSize(header_sz)
	t.setStyle(style_str)
	t.setFace(font)
	t.setTextColor(tag_color_str)
	t.draw(win)

	for x in range(0, days):
		for y in range(0, elem):
			t = Text(Point(x_coord, y_coord), w[x][y])
			t.setFace(font)
			t.setStyle(style_str)
			t.setSize(size)
			t.setTextColor(color_str)
			t.draw(win)
			if y == elem-1:
				# adding tag
				y_coord = y_coord + y_inc
				date = datetime.date.today() + datetime.timedelta(days=x)
				point = Point(x_coord, y_coord)
				t = Text(point, date.strftime('%A'))
				t.setSize(day_sz)
				t.setStyle(style_str)
				t.setFace(font)
				t.setTextColor(tag_color_str)
				t.draw(win)	
				# reset for next weather day
				x_coord = x_coord + x_inc
				y_coord = y_coord - y_inc * 2
			else:
				y_coord = y_coord + y_inc
			if x == 1 and y == 1: # after 2 days
				x_coord = start_x_coord
				y_coord = y_coord + newline_y_inc
			if x == 3 and y == 1: # last day goes in middle on bottom
				x_coord = bottom_x_coord
				y_coord = y_coord + newline_y_inc
		

def calendar(win):

	# variables
	font = "arial"
	style_str = "bold"
	color_str = "white"
	header_color_str = "yellow"
	header_str = "EVENTS"
	events = 2
	elem = 2
	size = 20
	header_x = 1095
	header_y = 450
	x_coord = 1095
	start_coord = 520
	decr = 25
	incr = 90
	no_more_events = 0
	header_sz = 24
	c = getCalendar(events)

	# header stuff

	point = Point(header_x, header_y)
	t = Text(point, header_str)
	t.setSize(header_sz)
	t.setStyle(style_str)
	t.setFace(font)
	t.setTextColor(header_color_str)
	t.draw(win)

	# actual events

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
	

def background(img_name, win):

	#create a point by specifying the x and y positions
	point1 = Point(680, 350) 
	# create image object
	image1 = Image(point1, img_name)
	#make it show up in the window
	image1.draw(win)



main()
