from pyA20.gpio import gpio as GPIO
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
import time

gpio.init()
gpio.setcfg(port.PA19, gpio.INPUT)
gpio.setcfg(port.PA18, gpio.INPUT)
while True:
  if gpio.input(port.PA19) == 0:
    print("19th button")
    time.sleep(0.5)
  if gpio.input(port.PA18) == 0:
    print("18th Button")
    time.sleep(0.5)
  if gpio.input(port.PA19) == 0 & gpio.input(port.PA18) == 0:
    print("death")
    time.sleep(0.5)
    
 


