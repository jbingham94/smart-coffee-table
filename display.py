from graphics import *
from smartCoffeeTable import *

'''
NOTES: 

Terra.gif settings are 400x400 anchor point



'''


def main():
    
    win = GraphWin("Smart Coffee Display",1365,900) 
    background_image="./static/26.gif"
    background(background_image, win)
    #cantor(600, 600, 60,win)
    #drawCircle(700,350,350,win)

    
    emailHeader("Email:", win)
    mail(win)


    # wait for mouse click to close window
    win.getMouse() # Pause to view result
    win.close()    # Close window when done




def mail(win):

	m = getMail(5)
	s = 270 # width for email text

	t0= Text(Point(s, 100), m[0][0])
	t0.setFace("courier")
	t0.setSize(16)
	t0.setTextColor("white")
	t0.draw(win)

	t1= Text(Point(s, 120), m[0][1])
	t1.setFace("courier")
	t1.setSize(16)
	t1.setTextColor("white")
	t1.draw(win)

	t3 = Text(Point(s, 140), m[0][2])
	t3.setFace("courier")
	t3.setSize(16)
	t3.setTextColor("white")
	t3.draw(win)

	t4 = Text(Point(s, 160), m[0][3])
	t4.setFace("courier")
	t4.setSize(16)
	t4.setTextColor("white")
	t4.draw(win)

	t5 = Text(Point(s, 195), m[0][4])
	t5.setFace("courier")
	t5.setSize(16)
	t5.setTextColor("white")
	t5.draw(win)


	
	t6= Text(Point(s, 230), m[1][0])
	t6.setFace("courier")
	t6.setSize(16)
	t6.setTextColor("white")
	t6.draw(win)

	t7= Text(Point(s, 250), m[1][1])
	t7.setFace("courier")
	t7.setSize(16)
	t7.setTextColor("white")
	t7.draw(win)

	t8 = Text(Point(s, 270), m[1][2])
	t8.setFace("courier")
	t8.setSize(16)
	t8.setTextColor("white")
	t8.draw(win)

	t9 = Text(Point(s, 290), m[1][3])
	t9.setFace("courier")
	t9.setSize(16)
	t9.setTextColor("white")
	t9.draw(win)

	t10 = Text(Point(s, 325), m[1][4])
	t10.setFace("courier")
	t10.setSize(16)
	t10.setTextColor("white")
	t10.draw(win)




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
