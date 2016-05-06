from boneHelpers import *

try:
	usrLEDs.write(15)
	waitSwitchStart("P9_42")
finally:
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()
