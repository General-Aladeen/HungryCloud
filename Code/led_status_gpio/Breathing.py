from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

gpio.init()

#LED 1 (TOP RIGHT)
led1R=OrangePwm(10, port.PA0)
led1G=OrangePwm(10, port.PA1)
led1B=OrangePwm(10,port.PA3)
#LED 2 (TOP RIGHT)
led2R =OrangePwm(10,port.PA13)
led2G =OrangePwm(10,port.PA10)
led2B =OrangePwm(10,port.PA2)
#LED 3 (BOTTOM LEFT)
led3R =OrangePwm(10,port.PA11)
led3G =OrangePwm(10,port.PA12)
led3B =OrangePwm(10,port.PA6)
#LED 4 (BOTTOM RIGHT)
led4R =OrangePwm(10,port.PA16)
led4G =OrangePwm(10,port.PA15)
led4B =OrangePwm(10,port.PA14)


i=1
led1R.start(0)
led1G.start(0)
led2R.start(0)
led2G.start(0)
led3R.start(0)
led3G.start(0)
led4R.start(0)
led4G.start(0)
try:
  while True:
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
except KeyboardInterrupt:
    led1R.stop()
    led2R.stop()
    led3R.stop()
    led4R.stop()
    print ("Done")

