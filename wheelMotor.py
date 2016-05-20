from boneHelpers  import *
from wheelEncoder import WheelEncoder

class WheelMotor(object):

	def __init__(self,fwdPinName,bwdPinName,speedPinName,encoderPinName):
		self.fwdPinName = fwdPinName
		self.bwdPinName = bwdPinName
		self.speedPinName = speedPinName
		if encoderPinName is not None:
			self._wheelEncoder = WheelEncoder(encoderPinName)
		else:
			self._wheelEncoder = None

	def setup(self):
		GPIO.setup(self.fwdPinName,GPIO.OUT,initial=LOW)
		GPIO.setup(self.bwdPinName,GPIO.OUT,initial=LOW)
		PWM.start(self.speedPinName)
		PWM.set_duty_cycle(0)
		if self._wheelEncoder is not None:
			self._wheelEncoder.setup()


	def reset(self):
		self._ticks = 0

	def getTicks(self):
		return self._ticks
	def _tickUpdate(self,channel):
		self._ticks += 1


