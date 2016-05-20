from boneHelpers import *
from kbHit       import KBHit
import sys

assert len(sys.argv) == 2,"Usage: testPwm pinName"

pinName = sys.argv[1]

dutyCycle = 0
freq      = 1000
print "[I] Testing PWM",pinName
print "[I] use 'a' 'z' keys to change dutyCycle"
print "[I] use 'q' 's' keys to change frequency"
def printPwmConf():
	print "[I] Freq : %6d Hz Duty : %3d%%"%(dutyCycle,freq)

kb = KBHit()
try:
	usrLEDs.write(15)
	PWM.start(pinName)
	PWM.set_duty_cycle(pinName,dutyCycle)
	PWM.set_frequency(pinName,freq)
	printPwmConf()
	while True:
		if kb.kbhit():
			c = kb.getch()
			if c in ('a','z','q','s'):
				if c == 'a' and dutyCycle>0  : dutyCycle -= 1
				if c == 'z' and dutyCycle<100: dutyCycle += 1
				if c == 'q' and freq>0:   freq -= 100
				if c == 's' and freq<1e6: freq += 100
				PWM.set_duty_cycle(pinName,dutyCyle)
				PWM.set_frequency(pinName,freq)
				printPwmConf()
			if ord(c) == 27:
				break
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()
	kb.set_normal_term()
