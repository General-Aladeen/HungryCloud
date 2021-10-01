from pyA20.gpio import gpio as GPIO

GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):

    print("Shutting Down")
 
GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

while 1:
    time.sleep(1)    
