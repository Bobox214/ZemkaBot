from Adafruit_BBIO import GPIO,PWM,ADC
from time import sleep,time

class UsrLEDs(object):
	def __init__(self):
		""" Ensure LEDs GPIOs are correctly configured """
		GPIO.setup("USR0",GPIO.OUT)
		GPIO.setup("USR1",GPIO.OUT)
		GPIO.setup("USR2",GPIO.OUT)
		GPIO.setup("USR3",GPIO.OUT)

	def write(self,val):
		""" Write a value between 0 and 15 to the 4 LEDs, considering them as bits """
		assert val>=0 and val<16
		GPIO.output("USR0",(val>>0)%2)
		GPIO.output("USR1",(val>>1)%2)
		GPIO.output("USR2",(val>>2)%2)
		GPIO.output("USR3",(val>>3)%2)

	def countdown(self):
		""" Do a 4 step countdown this the LED, each step is spaced by 1s """
		self.write(15)
		sleep(1)
		self.write(7)
		sleep(1)
		self.write(3)
		sleep(1)
		self.write(1)
		sleep(1)
		self.write(0)

	def reset(self):
		""" Reset the LEDs to their boot state, namely heartbeat/microSD/cpu/eMMC """
		for i,trigger in enumerate(['heartbeat','mmc0','cpu0','mmc1']):
			with open("/sys/class/leds/beaglebone:green:usr%s/trigger"%i,'w') as f:
				f.write(trigger)

usrLEDs = UsrLEDs()


def waitSwitchStart(switchPin):
	"""
		A Switch is connected to the provided pin.
		While waiting for the switch to be HIGH, USR LED are
		doing a one hot pattern.
		When the Switch is activated, a countdown is started.
	"""
	print("")
	print("[I] Waiting starting switch on %s"%switchPin)
	GPIO.setup(switchPin,GPIO.INPUT)

	t = time()
	while True:
		if GPIO.input(switchPin):
			print("[I] Countdown started")
			usrLedCountdown()
			break
		sleep(0.1)
		writeUsrLed(1<<(int(time()-t)%4))

	print("[I] Go Go Go !")

	
