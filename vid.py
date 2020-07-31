import cv2
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # the pin numbers refer to the board connector
cam = cv2.VideoCapture(0) # initialize the camera

MAGNET = 16               # pin number on raspberry pi GPIO
pathOut = 'video.mp4'     # output file name for video
fps = 2.0                 # frames per second to write to video
size = (1920,1080)        # dimensions of video
time_limit = 60           # time limit, in seconds

GPIO.setup(MAGNET, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set up pin as an input with a pull-up resistor
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
tic = time.perf_counter()
i = 1

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
            i += 1
            print("Image captured (%d)" % i)
    if (toc - tic) >= time_limit:
        break
    
out.release()
cam.release()
