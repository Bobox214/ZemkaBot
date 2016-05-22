"""
	Simply do a 'print value' test on the provided pin as argument.
	To be connected to a switch to test matching of name and pin
"""
from boneHelpers import *
from kbHit       import KBHit
from wheelMotor  import WheelMotor
import sys

assert len(sys.argv) == 4,"Usage: testWheelMotor fwdPinName bwdPinName speedPinName"

fwdPinName = sys.argv[1]
bwdPinName = sys.argv[2]
speedPinName = sys.argv[3]
speed = 0
kb = KBHit()
print "[I] Testing WheelMotor on ",fwdPinName,bwdPinName,speedPinName
print "[I] Use 'a' 'z' keys to change speed"
print "[I] Use 'q' 's' 'd' keys to change direction. This reduces speed to 0"
try:
	wheelMotor = WheelMotor(fwdPinName,bwdPinName,speedPinName)
	wheelMotor.setup()
	while True:
		if kb.kbhit():
			c = kb.getch()
			if c in ('a','z'):
				if c=='a' and speed>5:   speed -=5
				if c=='z' and speed<=95: speed +=5
				wheelMotor.setSpeed(speed)
				print '[I] Speed',speed
			if c in ('q','s','d'):
				speed = 0
				wheelMotor.setSpeed(speed)
				if c=='q': wheelMotor.backward(); print '[I] Going backward'
				if c=='s': wheelMotor.stop();     print '[I] Stopped'
				if c=='d': wheelMotor.forward();  print '[I] Going forward'
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()

