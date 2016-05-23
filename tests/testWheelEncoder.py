import context
from boneHelpers import *
from zemkaBot.wheelEncoder import WheelEncoder
import sys

assert len(sys.argv) == 2,"Usage: testWheelEncoder pinName"

pinName = sys.argv[1]
print "[I] Testing WheelEncoder on ",pinName
try:
	wheelEncoder = WheelEncoder(pinName)
	wheelEncoder.setup()
	while True:
		sleep(0.2)
		print "[I] Ticks : %6d . Speed  %4.3g ticks/s"%(wheelEncoder.getTicks(),wheelEncoder.getTpsSpeed())
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()

