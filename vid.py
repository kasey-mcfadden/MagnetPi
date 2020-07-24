import cv2
import numpy as np
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector not the chip
cam = cv2.VideoCapture(0) # initialize the camera

MAGNET = 16
pathOut = 'video.avi'
fps = 0.5
size = (1920,1080)

GPIO.setup(MAGNET, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up pin as an input with a pull-up resistor
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
tic = time.perf_counter()

while True:
    toc = time.perf_counter()
    isOpen = GPIO.input(MAGNET)
    
    if not isOpen:
        ret, image = cam.read()
        if ret:
            # cv2.imshow('SnapshotTest',image)
            # cv2.waitKey(0)
            # cv2.destroyWindow('SnapshotTest')
            # cv2.imwrite('SnapshotTest.jpg',image)
            out.write(image)
            print("Image captured")
    if (toc - tic) >= 30:
        break
    
out.release()
cam.release()