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
    print(intcheck)
    
def segs():
    print('Starting function return_zero()...')
    intcheck = 4
    return 0

f __name__ == '__main__':
    # counter is an infinite iterator
    counter = count(0)
    p1 = Process(target=intern, name='Process_inc_forever')
    p2 = Process(target=segs, name='Process_return_zero')
    p1.start()
    p2.start()
    p1.join(timeout=5)
    p2.join(timeout=5)
    p1.terminate()
    p2.terminate()
if p1.exitcode is None:
       print(f'Oops, {p1} timeouts!')
if p2.exitcode == 0:
        print(f'{p2} is luck and finishes in 5 seconds!')

