import context
from tools.beagleBoneBlack import *
import sys

assert len(sys.argv) == 2,"Usage: testGpioOutput pinName"

pinName = sys.argv[1]
print "[I] Testing GPIO",pinName

try:
	GPIO.setup(pinName,GPIO.OUT)
	usrLEDs.write(15)
	while True:
		GPIO.output(pinName,1)
		sleep(0.5)
		GPIO.output(pinName,0)
		sleep(0.5)
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()
