import context
from boneHelpers import *
from kbHit       import KBHit
from zemkaBot.wheel import Wheel
import sys

assert len(sys.argv) == 5,"Usage: testWheel fwdPinName bwdPinName speedPinName encoderPinName"

fwdPinName = sys.argv[1]
bwdPinName = sys.argv[2]
speedPinName = sys.argv[3]
encoderPinName = sys.argv[4]
speed = 0
kb = KBHit()
print "[I] Testing Wheel on ",fwdPinName,bwdPinName,speedPinName,encoderPinName
print "[I] Use 'a' 'z' keys to change speed"
print "[I] Use 's' to stop the wheel"

wheel = Wheel(fwdPinName,bwdPinName,speedPinName,encoderPinName)
try:
	wheel.setup()
	wheel.stop()
	while True:
		if kb.kbhit():
			c = kb.getch()
			if c in ('a','z'):
				if c=='a' and speed>-195: speed -=5
				if c=='z' and speed<=195: speed +=5
				wheel.setSpeed(speed)
				print '[I] Speed',speed
			if c=='s':
				wheel.stop()
				speed = 0
				print '[I] Stopped'
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	kb.set_normal_term()
	wheel.cleanup()
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()

