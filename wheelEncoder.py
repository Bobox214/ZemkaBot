from boneHelpers import *

class WheelEncoder(object):

	def __init__(self,pinName):
		self._pinName = pinName

	def setup(self):
		self.reset()
		GPIO.setup(self._pinName,GPIO.IN)
		GPIO.add_event_detect(self._pinName,GPIO.BOTH,callback=self._tickUpdate)

	def reset(self):
		self._lastTime  = time()
		self._lastTicks = 0
		self._ticks     = 0

	def getTicks(self):
		return self._ticks

	def getTpsSpeed(self):
		""" Return speed in ticks per seconds """
		_time = time()
		tpsSpeed = (self._ticks-self._lastTicks)/(_time-self._lastTime)
		self._lastTicks = self._ticks
		self._lastTime  = _time
		return tpsSpeed

	def _tickUpdate(self,channel):
		self._ticks += 1

	def cleanup(self):
		pass


