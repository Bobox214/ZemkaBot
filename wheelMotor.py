from boneHelpers  import *
from wheelEncoder import WheelEncoder

class WheelMotor(object):
	maxDuty = 100
	minDuty = 0

	def __init__(self,fwdPinName,bwdPinName,ctrlPinName):
		self.fwdPinName = fwdPinName
		self.bwdPinName = bwdPinName
		self.ctrlPinName = ctrlPinName

	def setup(self):
		GPIO.setup(self.fwdPinName,GPIO.OUT,initial=0)
		GPIO.setup(self.bwdPinName,GPIO.OUT,initial=0)
		PWM.start(self.ctrlPinName)
		PWM.set_frequency(self.ctrlPinName,5)
		PWM.set_duty_cycle(self.ctrlPinName,0)

	def forward(self):
		GPIO.output(self.fwdPinName,1)
		GPIO.output(self.bwdPinName,0)

	def backward(self):
		GPIO.output(self.fwdPinName,0)
		GPIO.output(self.bwdPinName,1)
	
	def stop(self):
		GPIO.output(self.fwdPinName,0)
		GPIO.output(self.bwdPinName,0)
		PWM.set_duty_cycle(self.ctrlPinName,0)
	
	def setCtrl(self,ctrl):
		ctrl = int(ctrl)
		if ctrl<self.minDuty: ctrl = self.minDuty
		if ctrl>self.maxDuty: ctrl = self.maxDuty
		PWM.set_duty_cycle(self.ctrlPinName,ctrl)

	def cleanup(self):
		PWM.stop(self.ctrlPinName)
