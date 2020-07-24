import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip

MAGNET = 16

GPIO.setup(MAGNET, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up pin as an input with a pull-up resistor

while True:
    isOpen = GPIO.input(MAGNET)
    
    if isOpen:
        print("Magnets open")
    else:
        print("Contact")
        
