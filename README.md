# MagnetPi

We'll be integrating a standard USB webcam and a magnetic sensor, with the help of a Raspberry Pi, in order to capture frames for tablet disintegration analysis.

Here's what we'll need:
- Raspberry Pi 3
- Monitor/TV
- HDMI Cord
- USB Keyboard
- USB Mouse
- USB Webcam
- Magnetic Contact Sensors
- Servo Tester
- M2M/M2F/F2F Breadboard Jumper Wires

## Configure the Raspberry Pi
Assemble the Raspberry Pi according to your starter kit. Connect your USB keyboard and mouse to the Raspberry Pi, connect it to a monitor via HDMI, and turn the power on. You'll see the Raspberry Pi desktop launch. From here, connect to a Wifi network, navigate to this repo, and download `vid.py` (either direct download or copy/paste into a new python file).

## Install OpenCV on the Raspberry Pi
Follow this [tutorial](https://pimylifeup.com/raspberry-pi-opencv/).
Reach out to me if you have any difficulties.

## Power up the servo
Connect three wires from the output side (signal/+/-) of your servo tester to the servo on your disintegration unit. Connect two (+/-) wires from the input side of the servo tester to pins 2(+) and 6(-) of the Raspberry Pi GPIO (general-purpose input/output) pins. After making sure the Raspberry Pi is on, ensure the servo tester lights up and can generate movement in the disintegration unit.

## Bring the magnets in
Using wires, connect your magnetic sensor to pins 14(-) and 16(+) on the Raspberry Pi GPIO. Mount the sensor (the one with wires) to the wall of the disintegration unit at the highest point in its vertical motion. Mount the magnet (the one without wires) to the white bar which raises and lowers the test tubes. The goal is for the sensor and magnet to overlap at the top of the vertical motion, creating contact and triggering the camera to take a snapshot.

## Set up the webcam
Use the hinge on the webcam to place it over the top of the disintegration unit, angled down and into the chamber for a clear picture of the disintegration process. Plug the webcam into a USB port on the Raspberry Pi.

## Fire it up
Open `vid.py` on the Raspberry Pi. It should open in Thonny, a Python IDE for the Raspberry Pi. From here you can run the code, generating videos for disintegration analysis. A few customizable fields:

```
MAGNET = 16               # pin number on raspberry pi GPIO
pathOut = 'video.mp4'     # output file name for video
fps = 2.0                 # frames per second to write to video
size = (1920,1080)        # dimensions of video
time_limit = 60           # time limit, in seconds
```
