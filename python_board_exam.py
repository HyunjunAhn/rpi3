import RPi.GPIO as GPIO
import time

LED = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED, GPIO.OUT)

try:
	while True:
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(0.5)

except KeyboardInterrupt:
	print "LED Test Terminated."
	GPIO.cleanup()

