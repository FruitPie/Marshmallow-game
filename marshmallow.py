import RPi.GPIO as GPIO
import time
import uinput

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
device = uinput.Device([uinput.KEY_A])

while True:
	if GPIO.input(2) == False:
		device.emit_click(uinput.KEY_A)
		print("marshmallow makes a good input")
	time.sleep(0.5)