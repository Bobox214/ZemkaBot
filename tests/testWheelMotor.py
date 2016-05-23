import context
from boneHelpers import *
from kbHit       import KBHit
from zemkaBot.wheelMotor import WheelMotor
import sys

assert len(sys.argv) == 4,"Usage: testWheelMotor fwdPinName bwdPinName speedPinName"

fwdPinName = sys.argv[1]
bwdPinName = sys.argv[2]
ctrlPinName = sys.argv[3]
ctrl = 0
kb = KBHit()
print "[I] Testing WheelMotor on ",fwdPinName,bwdPinName,ctrlPinName
print "[I] Use 'a' 'z' keys to change ctrl"
print "[I] Use 'q' 's' 'd' keys to change direction. This reduces ctrl to 0"
try:
	wheelMotor = WheelMotor(fwdPinName,bwdPinName,ctrlPinName)
	wheelMotor.setup()
	while True:
		if kb.kbhit():
			c = kb.getch()
			if c in ('a','z'):
				if c=='a' and ctrl>5:   ctrl -=5
				if c=='z' and ctrl<=95: ctrl +=5
				wheelMotor.setCtrl(ctrl)
				print '[I] Ctrl',ctrl
			if c in ('q','s','d'):
				ctrl = 0
				wheelMotor.setCtrl(ctrl)
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

