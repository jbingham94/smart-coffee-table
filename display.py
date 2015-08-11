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


from graphics import *
from smartCoffeeTable import *
import datetime
import time
import textwrap
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.IN)

def main():
    win = GraphWin("Smart Coffee Display", 1315, 703)
    win.setBackground("black")
    while True:
	if ( GPIO.input(10) == False ):
	    main_stuff(win)
	elif ( GPIO.input(10) == True ):
	    continue
	
def main_stuff(win):

    # set up background
    background_image = "./static/space.gif"
    backgd = background(background_image, win)

    # widget start points
    mail_x = 300
    mail_y = 100
    weather_x = 100
    weather_y = 520
    news_x = 1095
    news_y = 100
    cal_x = 1095
    cal_y = 520
    clock_x = 700
    clock_y = 333
    coff_x = 700
    coff_y = 400

    # widget bounds for click detection
    mail_width = 200
    mail_height = 350
    news_width = 200
    news_height = 410
    weather_width = 560
    weather_height = 230
    cal_width = 200
    cal_height = 200
    clock_width = 90
    clock_height = 13

    # offsets (also for click detection)
    weather_start_x = 70
    weather_start_y = 50
    news_start = 60
    cal_start = 50

    # boundaries of coffee icon
    coffee_left = 675
    coffee_right = 725
    coffee_top = 370
    coffee_bottom = 435

    # set up main modules
    mail_objs = mail(win, mail_x, mail_y)
    news_objs = news(win, news_x, news_y)
    cal_objs = calendar(win, cal_x, cal_y)
    weather_objs = weather(win, weather_x, weather_y)
    clock_obj = clock(win, clock_x, clock_y)
    coffee_cup = drawCoffee(coff_x, coff_y, win)

    # coffee cup movement standards
    right_move_dist = 300
    left_move_dist = -300
    up_dist = 200
    down_dist = -200

    # booleans for loop
    coffee_placed = 0
    green_drawn = 0

    # begin timer
    start_time = time.time()
    shutdown_time = 15 # in seconds
    
    # coffee cup placement
    var = 1
    while var == 1:
        # see if we go back to black
        curr_time = time.time()-start_time
        if curr_time >= shutdown_time:
            break
        # otherwise, continue
        click = win.checkMouse()
        if coffee_placed == 0 and click != None:
            if (click.getX() >= coffee_left and click.getX() <= coffee_right) and (click.getY() >= coffee_top and click.getY() <= coffee_bottom):
                coffee_cup.undraw()
                green = drawGreenCoffee(coff_x, coff_y, win)
                green_drawn = 1
                click = win.getMouse()  # get new mouse click
                # determine what to move & where
                if isModule(click.getX(), click.getY(), mail_x, mail_y, mail_width, mail_height, 1) == 1:
                    moduleMove(mail_objs, right_move_dist, "x")
                    mail_x = mail_x + right_move_dist
                    clockMove(clock_obj, down_dist, "y")
                    clock_y = clock_y - down_dist
                elif isModule(click.getX(), click.getY(), weather_x - weather_start_x, weather_y - weather_start_y, weather_width, weather_height, 0) == 1:
                    moduleMove(weather_objs, right_move_dist, "x")
                    weather_x = weather_x + right_move_dist
                elif isModule(click.getX(), click.getY(), news_x, news_y - news_start, news_width, news_height, 1) == 1:
                    moduleMove(news_objs, left_move_dist, "x")
                    news_x = news_x - left_move_dist
                    clockMove(clock_obj, down_dist, "y")
                    clock_y = clock_y - down_dist
                elif isModule(click.getX(), click.getY(), cal_x, cal_y - cal_start, cal_width, cal_height, 1) == 1:
                    moduleMove(cal_objs, left_move_dist, "x")
                    cal_x = cal_x - left_move_dist
                elif isClock(click.getX(), click.getY(), clock_x, clock_y, clock_width, clock_height) == 1:
                    clockMove(clock_obj, up_dist, "y")
                    clock_y = clock_y - up_dist
                else:
                    green.undraw()
                green.undraw()
                coffee_placed = 1
                green_drawn = 0
            else:
                continue
        elif green_drawn == 1:
            continue
        else:
            clock_obj.undraw()
            clock_obj = clock(win, clock_x, clock_y)
            time.sleep(1)
            clock_obj.undraw()

    for obj in mail_objs:
        obj.undraw()
    for obj in weather_objs:
        obj.undraw()
    for obj in cal_objs:
        obj.undraw()
    for obj in news_objs:
        obj.undraw()
    clock_obj.undraw()
    coffee_cup.undraw()
    backgd.undraw()

def drawCoffee(x, y, win):
    coffeeCup = Image(Point(x, y), "./static/coffee-cup.gif")
    coffeeCup.draw(win)
    return coffeeCup

def drawGreenCoffee(x, y, win):
    coffeeCup = Image(Point(x, y), "./static/coffee-cup-green.gif")
    coffeeCup.draw(win)
    return coffeeCup

def isModule(x, y, modX, modY, width, height, centered):
    if centered == 1:
        if (x >= modX - width and x <= modX + width) and (y >= modY and y <= modY + height):
            return 1
    elif centered == 0:
        if (x >= modX and x <= modX + width) and (y >= modY and y <= modY + height):
            return 1
    else:
        return 0

def isClock(x, y, modX, modY, width, height):
    if (x >= modX - width and x <= modX + width) and (y > modY - height and y <= modY + height):
        return 1
    else:
        return 0

def moduleMove(objects, distance, direction):
    if direction == "x":
        for x in objects:
            x.move(distance, 0)
    elif direction == "y":
        for x in objects:
            x.move(0, distance)

def clockMove(obj, distance, direction):
    if direction == "x":
        obj.move(distance, 0)
    elif direction == "y":
        obj.move(0, distance)

def clock(win, x_coord, y_coord):

    # displaying time
    time = datetime.datetime.now().time()
    time_str = time.strftime('%l:%M %p')
    t = Text(Point(x_coord, y_coord), time_str)
    t.setFace('times roman')
    t.setSize(30)
    t.setTextColor("green")
    t.draw(win)
    return t

# draws news module starting from passed x, y coordinates
def news(win, x_coord, y_coord):

    # variables
    obj_list = []
    font = "arial"
    effect_str = "bold"
    color_str = "white"
    header_color_str = "yellow"
    header_str = "NEWS"
    stor_num = 5
    size = 11
    sm_incr = 30
    mid_incr = 40
    big_incr = 50
    stories = 3
    elem = 3
    header_x = x_coord
    header_y = y_coord - 50
    header_sz = 24
    line_lim = 55
    n = getNews(stor_num)

    # header stuff
    point = Point(header_x, header_y)
    t = Text(point, header_str)
    t.setSize(header_sz)
    t.setStyle(effect_str)
    t.setFace(font)
    t.setTextColor(header_color_str)
    t.draw(win)
    obj_list.append(t)

    # stories

    for x in range(0, stories ):
        for y in range(0, elem):
            t = Text(Point(x_coord, y_coord), textwrap.fill(n[x][y], line_lim))
            t.setFace(font)
            if y == 0:
                t.setStyle(effect_str)
            t.setSize(size)
            t.setTextColor(color_str)
            t.draw(win)
            obj_list.append(t)
            if y == elem - 1:
                y_coord = y_coord + 55
            elif y == elem - 2:
                y_coord = y_coord + 45
            else:
                y_coord = y_coord + sm_incr

    return obj_list

# draws mail module starting from passed x, y coordinates
def mail(win, x_coord, y_coord):

    # variables
    obj_list = []
    header_style = "bold"
    header_text = "EMAIL"
    header_color_str = "yellow"
    font = "arial"
    color_str = "white"
    emails = 4
    header_x = x_coord
    header_y = y_coord - 50
    header_size = 24
    max_body = 55
    sm_incr = 15
    mid_incr = 20
    big_incr = 50
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
    obj_list.append(t)

    # displaying emails
    for x in range(emails-1, -1, -1):  # grab emails by most recent
        for y in range(0, elem):
            if y == elem - 1 and len(m[x][y]) > max_body: # deals with longer email bodies
                head_len = 0
                if "\n" in m[x][y]:
                    head, sep, tail = m[x][y].partition('\n')
                    head_len = len(head)
                body_str = head[0:head_len-1] + "..."
                print body_str
                t = Text(Point(x_coord, y_coord), body_str)
            else:
                t = Text(Point(x_coord, y_coord), m[x][y])
            t.setFace(font)
            t.setSize(font_sz)
            t.setTextColor(color_str)
            if y == subj_slot:
                t.setStyle(header_style)
            t.draw(win)
            obj_list.append(t)
            if y == elem-2:  # second to last element in email
                y_coord = y_coord + big_incr
            elif y == elem-1:  # last element in email
                y_coord = y_coord
            else:
                y_coord = y_coord + mid_incr

    return obj_list

def weather(win, x_coord, y_coord):

    obj_list = []
    zipcode = "03755"
    font = "arial"
    style_str = "bold"
    color_str = "white"
    tag_color_str = "yellow"
    header_str = "WEATHER"
    size = 20
    start_x_coord = x_coord
    start_y_coord = y_coord
    bottom_x_coord = x_coord + 100
    x_inc = 190
    y_inc = 30
    newline_y_inc = 90
    days = 5
    elem = 2
    w = getWeather(zipcode)
    style_str = "bold"
    font = "arial"
    header_sz = 24
    day_sz = 16
    max_len = 15
    # for header
    header_x = x_coord + 200
    header_y = y_coord - 40

    # header setup
    point = Point(header_x, header_y)
    t = Text(point, header_str)
    t.setSize(header_sz)
    t.setStyle(style_str)
    t.setFace(font)
    t.setTextColor(tag_color_str)
    t.draw(win)
    obj_list.append(t)

    for x in range(0, days):
        for y in range(0, elem):
            if y == elem-1: # adding degrees signs
                u = u"\N{DEGREE SIGN}" 
                temp = u + "F"
                temp_str = w[x][y] + temp
                t = Text(Point(x_coord, y_coord),temp_str)
            elif y == elem-2 and len(w[x][y]) > max_len:
                weather_str = w[x][y].split(' ',1)[0]
                t = Text(Point(x_coord, y_coord), weather_str)
                t.setStyle(style_str)
            else:
                t = Text(Point(x_coord, y_coord),w[x][y])
                t.setStyle(style_str)
            t.setFace(font)
            t.setSize(size)
            t.setTextColor(color_str)
            t.draw(win)
            obj_list.append(t)
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
                obj_list.append(t)
                # reset for next weather day
                x_coord = x_coord + x_inc
                y_coord = y_coord - y_inc * 2
            else:
                y_coord = y_coord + y_inc
            if x == 2 and y == 1:  # after 3 days
                x_coord = bottom_x_coord
                y_coord = y_coord + newline_y_inc

    return obj_list


def calendar(win, x_coord, y_coord):

    # variables
    obj_list = []
    font = "arial"
    style_str = "bold"
    color_str = "white"
    header_color_str = "yellow"
    header_str = "EVENTS"
    events = 3
    elem = 2
    size = 16
    header_x = x_coord
    header_y = y_coord - 30
    decr = 25
    incr = 80
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
    obj_list.append(t)

    # actual events

    for x in range(0, events):
        if no_more_events == 1:
            break
        if x == 0:
            y_coord = y_coord + 30
        for y in range(0, elem):
            if c[x][y] == 0:
                no_more_events = 1
                break
            t = Text(Point(x_coord, y_coord), c[x][y])
            t.setFace(font)
            if y == 1:
                t.setStyle(style_str)
            t.setSize(size)
            t.setTextColor(color_str)
            t.draw(win)
            obj_list.append(t)
            if y == elem - 1:
                y_coord = y_coord + incr
            else:
                y_coord = y_coord - decr

    return obj_list

def background(img_name, win):

    #create a point by specifying the x and y positions
    point1 = Point(680, 350)
    # create image object
    image1 = Image(point1, img_name)
    #make it show up in the window
    image1.draw(win)
    return image1


main()
