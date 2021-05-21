from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
from orangepwm import *

gpio.init()

pwm = OrangePwm(100, port.PA6)

pwm.start(20)
sleep(2)

pwm.changeDutyCycle(6)
sleep(2)

pwm.changeFrequency(10)
sleep(2)

pwm.stop()
