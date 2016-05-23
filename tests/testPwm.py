import context
from tools.beagleBoneBlack import *
from tools.kbHit           import KBHit
import sys

assert len(sys.argv) >= 2,"Usage: testPwm pinName1 [pinName2 .. pinName3]"

pinNames = sys.argv[1:]

dutyCycle = 60
freq      = 5
print "[I] Testing PWM",pinNames
print "[I] use 'a' 'z' keys to change dutyCycle"
print "[I] use 'q' 's' keys to change frequency"
def printPwmConf():
	print "[I] Freq : %6d Hz Duty : %3d"%(freq,dutyCycle)

kb = KBHit()
try:
	usrLEDs.write(15)
	for pinName in pinNames:
		PWM.start(pinName)
		PWM.set_duty_cycle(pinName,dutyCycle)
		PWM.set_frequency(pinName,freq)
	printPwmConf()
	while True:
		if kb.kbhit():
			c = kb.getch()
			if c in ('a','z','q','s'):
				if c == 'a' and dutyCycle>0  : dutyCycle -= 5
				if c == 'z' and dutyCycle<100: dutyCycle += 5
				if c == 'q' and freq>0:   freq -= 1
				if c == 's' and freq<1e6: freq += 1
				for pinName in pinNames:
					PWM.set_frequency(pinName,freq)
					PWM.set_duty_cycle(pinName,dutyCycle)
				printPwmConf()
			if ord(c) == 27:
				break
		sleep(0.1)
except KeyboardInterrupt:
	pass
finally:
	print "[I] Cleaning"
	usrLEDs.reset()
	GPIO.cleanup()
	PWM.cleanup()
	kb.set_normal_term()
