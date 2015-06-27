import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)

now = time.time()
future = now + 10
score = 1

while time.time() < future:

	while True:
		if GPIO.input(2) == False:
			print(score)
			time.sleep(0.5)
			score = score + 1
			break
	
else:
	#print (score + "points")
	print("Game over!")