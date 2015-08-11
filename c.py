import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(10,GPIO.IN)


while True:
	if ( GPIO.input(10) == False ):
		print ("BUTTON PRESSED")
		os.system('date')
		time.sleep(2)
	elif ( GPIO.input(10) == True ):
		os.system('clear')
		print("Waiting...")


time.sleep(5)




















