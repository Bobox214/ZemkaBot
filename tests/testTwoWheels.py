from boneHelpers import *
from kbHit       import KBHit
from wheel       import Wheel
import sys

assert len(sys.argv) == 9,"Usage: testWheel fwdPinName1 bwdPinName1 speedPinName1 encoderPinName1 fwdPinName2 bwdPinName2 speedPinName2 encoderPinName2"

fwdPinName1 = sys.argv[1]
bwdPinName1 = sys.argv[2]
speedPinName1 = sys.argv[3]
encoderPinName1 = sys.argv[4]
fwdPinName2 = sys.argv[5]
bwdPinName2 = sys.argv[6]
speedPinName2 = sys.argv[7]
encoderPinName2 = sys.argv[8]

speed = 0
kb = KBHit()
print "[I] Testing Two wheels on "
print "[I] Use 'a' 'z' keys to change speed"
print "[I] Use 's' to stop the wheel"

wheels = [
	Wheel(fwdPinName1,bwdPinName1,speedPinName1,encoderPinName1)
,	Wheel(fwdPinName2,bwdPinName2,speedPinName2,encoderPinName2)
]
try:
	for wheel in wheels:
		wheel.setup()
		wheel.stop()
	while True:
		if kb.kbhit():
			c = kb.getch()
			if c in ('a','z'):
				if c=='a' and speed>-115: speed -=5
				if c=='z' and speed<=115: speed +=5
				for wheel in wheels:
					wheel.setSpeed(speed)
				print '[I] Speed',speed
			if c=='s':
				for wheel in wheels:
					wheel.stop()
				speed = 0
				print '[I] Stopped'
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	kb.set_normal_term()
	for wheel in wheels:
		wheel.cleanup()
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()

