from boneHelpers  import *
from wheelEncoder import WheelEncoder

class WheelMotor(object):

	def __init__(self,fwdPinName,bwdPinName,speedPinName):
		self.fwdPinName = fwdPinName
		self.bwdPinName = bwdPinName
		self.speedPinName = speedPinName

	def setup(self):
		GPIO.setup(self.fwdPinName,GPIO.OUT,initial=0)
		GPIO.setup(self.bwdPinName,GPIO.OUT,initial=0)
		PWM.start(self.speedPinName)
		PWM.set_frequency(self.speedPinName,5)
		PWM.set_duty_cycle(self.speedPinName,0)

	def forward(self):
		GPIO.output(self.fwdPinName,1)
		GPIO.output(self.bwdPinName,0)

	def backward(self):
		GPIO.output(self.fwdPinName,0)
		GPIO.output(self.bwdPinName,1)
	
	def stop(self):
		GPIO.output(self.fwdPinName,0)
		GPIO.output(self.bwdPinName,0)
	
	def setSpeed(self,speed):
		assert speed>=0 and speed<=100, "Min 0 , Max 100"
		PWM.set_duty_cycle(self.speedPinName,speed)

	def cleanup(self):
		PWM.stop(self.speedPinName)

		
