import context
from tools.beagleBoneBlack import *
import sys

assert len(sys.argv) == 2,"Usage: testGpioInput pinName"

def printValue(channel):
	print "[I] Event on ",channel," Value: ",GPIO.input(channel)

pinName = sys.argv[1]
print "[I] Testing GPIO",pinName
try:
	GPIO.setup(pinName,GPIO.IN)
	GPIO.add_event_detect(pinName,GPIO.BOTH,callback=printValue)
	usrLEDs.write(15)
	while True:
		sleep(1)
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()

