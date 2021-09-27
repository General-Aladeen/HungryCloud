from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

#hi
gpio.init ()

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


#----------Init----------#
gpio.setcfg (led1R, gpio.OUTPUT)
gpio.setcfg (led1G, gpio.OUTPUT)
gpio.setcfg (led1B, gpio.OUTPUT)

gpio.setcfg (led2R, gpio.OUTPUT)
gpio.setcfg (led2G, gpio.OUTPUT)
gpio.setcfg (led2B, gpio.OUTPUT)

gpio.setcfg (led3R, gpio.OUTPUT)
gpio.setcfg (led3G, gpio.OUTPUT)
gpio.setcfg (led3B, gpio.OUTPUT)

gpio.setcfg (led4R, gpio.OUTPUT)
gpio.setcfg (led4G, gpio.OUTPUT)
gpio.setcfg (led4B, gpio.OUTPUT)


gpio.output (led1R, gpio.HIGH)
gpio.output (led1G, gpio.HIGH)
gpio.output (led1B, gpio.HIGH)
gpio.output (led2R, gpio.HIGH)
gpio.output (led2G, gpio.HIGH)
gpio.output (led2B, gpio.HIGH)
gpio.output (led3R, gpio.HIGH)
gpio.output (led3G, gpio.HIGH)
gpio.output (led3B, gpio.HIGH)
gpio.output (led4R, gpio.HIGH)
gpio.output (led4G, gpio.HIGH)
gpio.output (led4B, gpio.HIGH)
