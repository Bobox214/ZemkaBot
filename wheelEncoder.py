from boneHelpers import *
class WheelEncoder(object):

	def __init__(self,pinName):
		self.pinName = pinName

	def setup(self):
		self.reset()
		GPIO.setup(self.pinName,GPIO.IN)
		GPIO.add_event_detect(self.pinName,GPIO.BOTH,callback=self._tickUpdate)

	def reset(self):
		self._ticks = 0

	def getTicks(self):
		return self._ticks
	def _tickUpdate(self,channel):
		self._ticks += 1


