"""
	Simply do a 'print value' test on the provided pin as argument.
	To be connected to a switch to test matching of name and pin
"""
from boneHelpers import *
from wheelEncoder import WheelEncoder
import sys

assert len(sys.argv) == 2,"Usage: testWheelEncoder pinName"

pinName = sys.argv[1]
print "[I] Testing WheelEncoder on ",pinName
try:
	wheelEncoder = WheelEncoder(pinName)
	wheelEncoder.setup()
	while True:
		sleep(0.2)
		print "[I] Ticks : ",wheelEncoder.getTicks()
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()

