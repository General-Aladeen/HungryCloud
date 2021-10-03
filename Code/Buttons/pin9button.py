from pyA20.gpio import gpio as GPIO
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
import time

gpio.init()
gpio.setcfg(port.PA19, gpio.INPUT)

while True:
  if gpio.input(port.PA19) == 0:
    print("ze button is pressed")
    time.sleep(0.1)


