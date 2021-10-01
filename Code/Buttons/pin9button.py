from pyA20.gpio import gpio as GPIO
from pyA20.gpio import gpio
from pyA20.gpio import port

gpio.init()
gpio.setcfg(port.PG9, gpio.INPUT)
var = port.PG9
print var
