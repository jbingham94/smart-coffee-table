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
import textwrap

def main():

    # make window
    win = GraphWin("Smart Coffee Display", 1315, 703)

    # set up background
    background_image = "./static/space.gif"
    background(background_image, win)

    mail_x = 300
    mail_y = 100
    weather_x = 100
    weather_y = 520
    news_x = 1095
    news_y = 100
    cal_x = 1095
    cal_y = 520
    clock_x = 682
    clock_y = 333

    # set up main modules
    mail_objs = mail(win, mail_x, mail_y)
    news_objs = news(win, news_x, news_y)
    cal_objs = calendar(win, cal_x, cal_y)
    weather_objs = weather(win, weather_x, weather_y)
    clock_obj = clock(win, clock_x, clock_y)
    place_txt = coffeePlace(win)

    right_move_dist = 300
    left_move_dist = -300
    up_dist = 200
    down_dist = -200

    # coffee cup placement
    var = 1
    while var == 1:
        click = win.getMouse()  # check if user clicks on coffee cup message
        if (click.getX() >= 550 and click.getX() <= 600) and (click.getY() >= 0 and click.getY() <= 100):
            place_txt.undraw()  # undraw initial message, replace with instruction
            instr = coffeeInstructions(win)
            click = win.getMouse()  # get new mouse click
            # determine what to move & where
            if isModule(click.getX(), click.getY(), mail_x, mail_y, 200, 350, 1) == 1:
                moduleMove(mail_objs, right_move_dist, "x")
                mail_x = mail_x + right_move_dist
                clockMove(clock_obj, down_dist, "y")
                clock_y = clock_y - down_dist
            elif isModule(click.getX(), click.getY(), weather_x - 70, weather_y - 50, 560, 230, 0) == 1:
                moduleMove(weather_objs, right_move_dist, "x")
                weather_x = weather_x + right_move_dist
            elif isModule(click.getX(), click.getY(), news_x, news_y - 60, 200, 410, 1) == 1:
                moduleMove(news_objs, left_move_dist, "x")
                news_x = news_x - left_move_dist
                clockMove(clock_obj, down_dist, "y")
                clock_y = clock_y - down_dist
            elif isModule(click.getX(), click.getY(), cal_x, cal_y - 50, 200, 200, 1) == 1:
                moduleMove(cal_objs, left_move_dist, "x")
                cal_x = cal_x - left_move_dist
            elif isClock(click.getX(), click.getY(), clock_x, clock_y) == 1:
                clockMove(clock_obj, up_dist, "y")
                clock_y = clock_y - up_dist
            else:
                instr.undraw()
            instr.undraw()
            break

    var = 1
    while var == 1:
        click = win.getMouse()
        print click.getX()
        print click.getY()
        
    # create continuous loop to make running clock
    clock_obj.undraw()
    var = 1
    while var == 1:
        obj = clock(win, clock_x, clock_y)
        time.sleep(1)
        obj.undraw()
    win.close()    # Close window when done

def isModule(x, y, modX, modY, width, height, centered):
    if centered == 1:
        if (x >= modX - width and x <= modX + width) and (y >= modY and y <= modY + height):
            return 1
    elif centered == 0:
        if (x >= modX and x <= modX + width) and (y >= modY and y <= modY + height):
            return 1
    else:
        return 0

def isClock(x, y, modX, modY):
    clock_size = 100
    if (x >= modX and x <= modX + clock_size) and (y > modY and y <= modY + clock_size):
        print "yes!"
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

def coffeePlace(win):
    msg = "Click HERE to place your coffee."
    t = Text(Point(668, 50), msg)
    t.setFace('arial')
    t.setSize(30)
    t.setTextColor("green")
    t.draw(win)
    return t

def coffeeInstructions(win):
    msg = "Now, click where you want it."
    t = Text(Point(668, 50), msg)
    t.setFace('arial')
    t.setStyle("bold")
    t.setSize(30)
    t.setTextColor("green")
    t.draw(win)
    return t

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
            t = Text(Point(x_coord, y_coord), textwrap.fill(n[x][y], 55))
            t.setFace(font)
            if y == 0:
                t.setStyle(effect_str)
            t.setSize(size)
            t.setTextColor(color_str)
            t.draw(win)
            obj_list.append(t)
            if y == elem - 1:
                y_coord = y_coord + big_incr
            elif y == elem - 2:
                y_coord = y_coord + mid_incr
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
    header_y = y_coord - 40
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


main()
