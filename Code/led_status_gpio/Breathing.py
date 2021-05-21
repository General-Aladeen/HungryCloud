from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

gpio.init()
pwm = OrangePwm(100, port.PA6)
i=1
pwm.start(0)
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
    

