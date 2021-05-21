#RGB values in %
R = input('R = ')
G = input('G = ')
B = input('B = ')

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


R = 100-R
G = 100-G
B = 100-B

led1R.start(R)
led1G.start(G)
led1B.start(B)

led2R.start(R)
led2G.start(G)
led2B.start(B)

led3R.start(R)
led3G.start(G)
led3B.start(B)

led4R.start(R)
led4G.start(G)
led4B.start(B)

except KeyboardInterrupt:
    led1R.stop()
    led1G.stop()
    led1B.stop()
    led2R.stop()
    led2G.stop()
    led2B.stop()
    led3R.stop()
    led3G.stop()
    led3B.stop()
    led4R.stop()
    led4G.stop()
    led4B.stop()
    print ("Done")















