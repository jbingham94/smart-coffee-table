from graphics import *



def main():
    
    win = GraphWin("Smart Coffee Display",1365,900)
    background_image="./static/terra.gif"
    back(background_image, win)
    #cantor(600, 600, 60,win)
    #drawCircle(700,350,350,win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done





def back(img_name, win):

	#create a point by specifying the x and y positions
	point1 = Point(400, 400)
	# create image object
	image1 = Image(point1, img_name)
	#make it show up in the window
	image1.draw(win)



def background(imag, win):
	
	p = Point(40,40)
	i = Image("lone_converted.gif")
	i.draw(win)
	








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
