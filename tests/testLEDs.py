import context
from tools.beagleBoneBlack import *

try:
	for i in range(5):
		usrLEDs.write(10)
		sleep(0.3)
		usrLEDs.write(5)
		sleep(0.3)
	usrLEDs.countdown()
finally:
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()
