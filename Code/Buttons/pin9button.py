from pyA20.gpio import gpio as GPIO
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector


gpio.init()
gpio.setcfg(port.PA19, gpio.INPUT)
var = port.PA19
print var
