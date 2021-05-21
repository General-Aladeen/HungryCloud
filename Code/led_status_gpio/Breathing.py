from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

gpio.init()

#LED 1 (TOP RIGHT)
led1R=port.PA0
led1G=port.PA1
led1B=port.PA3
#LED 2 (TOP RIGHT)
led2R = port.PA13
led2G = port.PA10
led2B = port.PA2
#LED 3 (BOTTOM LEFT)
led3R = port.PA11
led3G = port.PA12
led3B = port.PA6
#LED 4 (BOTTOM RIGHT)
led4R = port.PA16
led4G = port.PA15
led4B = port.PA14

pwm = OrangePwm(100, led1R)
pwm = OrangePwm(100, led1G)
pwm = OrangePwm(100, led1B)

pwm = OrangePwm(100, led2R)
pwm = OrangePwm(100, led2G)
pwm = OrangePwm(100, led2B)

pwm = OrangePwm(100, led3R)
pwm = OrangePwm(100, led3G)
pwm = OrangePwm(100, led3B)

pwm = OrangePwm(100, led4R)
pwm = OrangePwm(100, led4G)
pwm = OrangePwm(100, led4B)


i=1
pwm.start(led1R,0)
try:
  while True:
    if i !=100:
      while i!=100:
        pwm.changeDutyCycle(i)
        sleep(0.01)
        i=i+1
    else :
      while i!=0:
        pwm.changeDutyCycle(i)
        sleep(0.006)
        i=i-1
except KeyboardInterrupt:
    pwm.stop()
    print ("Done")

