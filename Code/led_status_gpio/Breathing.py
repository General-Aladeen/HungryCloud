from pyA20.gpio import gpio as GPIO
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import threading
import time
import urllib
class OrangePwm(threading.Thread):

  def __init__(self, frequency, gpioPin, gpioScheme=0):
     """ 
     Init the OrangePwm instance. Expected parameters are :
     - frequency : the frequency in Hz for the PWM pattern. A correct value may be 100.
     - gpioPin : the gpio.port which will act as PWM ouput
     - gpioScheme : saved for compatibility with PiZyPWM code
     """
     self.baseTime = 1.0 / frequency
     self.maxCycle = 100.0
     self.sliceTime = self.baseTime / self.maxCycle
     self.gpioPin = gpioPin
     self.terminated = False
     self.toTerminate = False
     #GPIO.setmode(gpioScheme)


  def start(self, dutyCycle):
    """
    Start PWM output. Expected parameter is :
    - dutyCycle : percentage of a single pattern to set HIGH output on the GPIO pin
    
    Example : with a frequency of 1 Hz, and a duty cycle set to 25, GPIO pin will 
    stay HIGH for 1*(25/100) seconds on HIGH output, and 1*(75/100) seconds on LOW output.
    """
    self.dutyCycle = dutyCycle
    GPIO.setcfg(self.gpioPin, GPIO.OUTPUT)
    self.thread = threading.Thread(None, self.run, None, (), {})
    self.thread.start()


  def run(self):
    """
    Run the PWM pattern into a background thread. This function should not be called outside of this class.
    """
    while self.toTerminate == False:
      if self.dutyCycle > 0:
        GPIO.output(self.gpioPin, GPIO.HIGH)
        time.sleep(self.dutyCycle * self.sliceTime)
      
      if self.dutyCycle < self.maxCycle:
        GPIO.output(self.gpioPin, GPIO.LOW)
        time.sleep((self.maxCycle - self.dutyCycle) * self.sliceTime)

    self.terminated = True


  def changeDutyCycle(self, dutyCycle):
    """
    Change the duration of HIGH output of the pattern. Expected parameter is :
    - dutyCycle : percentage of a single pattern to set HIGH output on the GPIO pin
    
    Example : with a frequency of 1 Hz, and a duty cycle set to 25, GPIO pin will 
    stay HIGH for 1*(25/100) seconds on HIGH output, and 1*(75/100) seconds on LOW output.
    """
    self.dutyCycle = dutyCycle


  def changeFrequency(self, frequency):
    """
    Change the frequency of the PWM pattern. Expected parameter is :
    - frequency : the frequency in Hz for the PWM pattern. A correct value may be 100.
    
    Example : with a frequency of 1 Hz, and a duty cycle set to 25, GPIO pin will 
    stay HIGH for 1*(25/100) seconds on HIGH output, and 1*(75/100) seconds on LOW output.
    """
    self.baseTime = 1.0 / frequency
    self.sliceTime = self.baseTime / self.maxCycle

  def stop(self):
    """
    Stops PWM output.
    """
    self.toTerminate = True
    while self.terminated == False:
      # Just wait
      time.sleep(0.01)
  
    GPIO.output(self.gpioPin, GPIO.LOW)
    GPIO.setcfg(self.gpioPin, GPIO.INPUT)
    

gpio.init()
#text to faix bug lmao ^.^ 
#LED 1 (TOP RIGHT)
led1R=OrangePwm(100, port.PA0)
led1G=OrangePwm(100, port.PA1)
led1B=OrangePwm(100,port.PA3)
#LED 2 (TOP RIGHT)
led2R =OrangePwm(100,port.PA13)
led2G =OrangePwm(100,port.PA10)
led2B =OrangePwm(100,port.PA2)
#LED 3 (BOTTOM LEFT)
led3R =OrangePwm(100,port.PA11)
led3G =OrangePwm(100,port.PA12)
led3B =OrangePwm(100,port.PA6)
#LED 4 (BOTTOM RIGHT)
led4R =OrangePwm(100,port.PA16)
led4G =OrangePwm(100,port.PA15)
led4B =OrangePwm(100,port.PA14)

led1G.start(100)
#led1G.start(0)
led2G.start(100)
#led2G.start(0)
led3G.start(100)
#led3G.start(0)
led4G.start(100)
#led4G.start(0)
led1R.start(100)
#led1G.start(0)
led2R.start(100)
#led2G.start(0)
led3R.start(100)
#led3G.start(0
led4R.start(100)
#led4G.start(0)


while True:
	
	try :
		stri = "https://www.google.co.in"
		data = urllib.urlopen(stri)
		beep = 1
	except:
		beep = 0
	print (beep)
	if beep == 0:

		if i !=100:
			while i!=100:
				led1R.changeDutyCycle(i)
				led2R.changeDutyCycle(i)
				led3R.changeDutyCycle(i)
				led4R.changeDutyCycle(i)
				sleep(0.01)
				i=i+1
		else :
		 while i!=0:
				led1R.changeDutyCycle(i)
				led2R.changeDutyCycle(i)
				led3R.changeDutyCycle(i)
				led4R.changeDutyCycle(i)
				sleep(0.006)
				i=i-1
	else:

		led1G.changeDutyCycle(0)
		led2G.changeDutyCycle(0)
		led3G.changeDutyCycle(0)
		led4G.changeDutyCycle(0)
