import urllib
import time
from itertools import count
from multiprocessing import Process
def intern():
    try :
        stri = "https://www.google.co.in"
        data = urllib.urlopen(stri)
        intcheck = 1
    except:
        intcheck = 0
    print (intcheck)
def segs():
    b=0
    while b != 10 :
        b = b+1       
        time.sleep(1) 
        print(b)
    return b   


i=0
while i == 0:
    if __name__ == '__main__':
        # counter is an infinite iterator
        counter = count(0)
        p1 = Process(target=intern, name='Process_inc_forever')
        p2 = Process(target=segs, name='Process_return_zero')
        p1.start()
        p2.start()
        time.sleep(12)
        if b == 10:
          p1.terminate
        p2.terminate
