from threading import Timer
from tools.beagleBoneBlack import *
import wheelMotor
import wheelEncoder

class Wheel(object):
	def __init__(self,fwdPinName,bwdPinName,speedPinName,encoderPinName):
		self._motor    = wheelMotor.WheelMotor(fwdPinName,bwdPinName,speedPinName)
		self._encoder  = wheelEncoder.WheelEncoder(encoderPinName)
		self._rpmSpeed = 0
		# Hardware configuration
		self._tpr = 390 #Ticks per rotation
		# Controller configuration
		self._Kp = 0.3  # Proportional gain
		self._Ki = 0.01 # Integral gain
		self._Kd = 0    # Derivative gain
		
		# Controller variables
		self._timer        = None
		self._motorCtrl    = 0
		self._lastRpmError = 0
		self._lastTime     = 0
		self._totRpmError  = 0
	
	def _stopMotor(self):
		self._motorCtrl    = 0
		self._lastRpmError = 0
		self._lastTime     = 0
		self._totRpmError  = 0
		self._motor.stop()
	
	def setup(self):
		self._motor.setup()
		self._encoder.setup()

	def cleanup(self):
		if self._timer is not None:
			self._timer.cancel()
		self._stopMotor()
		self._motor.cleanup()
		self._encoder.cleanup()

	def configureHardware(self,ticksPerRotation):
		self._tpr = ticksPerRotation

	def configureController(self,Kp,Ki,Kd):
		self._Kp = Kp
		self._Ki = Ki
		self._Kd = Kd

	def _controller(self):
		if self._rpmSpeed == 0:
			self._stopMotor()
			return
		# Timer to recal ourself
		if self._timer is not None:
			self._timer.cancel()
		self._timer = Timer(0.3,self._controller)
		self._timer.start()

		# Time Delta dt
		if self._lastTime == 0:
			print "[I] Restart"
			self._lastTime = time()
			dt = 0
		else:
			t = time()
			dt = t-self._lastTime
			self._lastTime = t
		
		# Error
		rpmSpeed = (self._encoder.getTpsSpeed()/self._tpr)*60
		pRpmError = self._rpmSpeed-rpmSpeed
		dRpmError = (pRpmError-self._lastRpmError)/dt if dt!=0 else 0
		iRpmError = self._totRpmError+pRpmError*dt

		self._lastRpmError = pRpmError
		self._totRpmError  = iRpmError

		# Motor Ctrl
		self._motorCtrl = self._motorCtrl+self._Kp*pRpmError+self._Kd*dRpmError+self._Ki*iRpmError
		self._motor.setCtrl(self._motorCtrl)
		print '[I] SPD %4d RPM %4d  pE %4d pI %4d pD %4d  Motor %d'%(self._rpmSpeed,rpmSpeed,pRpmError,iRpmError,dRpmError,self._motorCtrl)
	
	def stop(self):
		self._rpmSpeed = 0
		self._controller()

	def setSpeed(self,rpmSpeed):
		if rpmSpeed == 0:
			self.stop()
			return
		if self._rpmSpeed == 0:
			if rpmSpeed>0:
				self._motor.forward()
			else:
				self._motor.backward()
			self._rpmSpeed =  abs(rpmSpeed)
			self._controller()
		else:
			self._rpmSpeed =  abs(rpmSpeed)
