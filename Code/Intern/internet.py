import urllib2
import socket
import multiprocessing as mp

def timeout(t, cmd, *args, **kwds):
    pool = mp.Pool(processes=1)
    result = pool.apply_async(cmd, args=args, kwds=kwds)
    try:
        retval = result.get(timeout=t)
    except mp.TimeoutError as err:
        pool.terminate()
        pool.join()
        raise
    else:
        return retval

def open(url):
    response = urllib2.urlopen(url)
   

url = 'https://www.google.com/'
try:
    timeout(5, open, url)
    print('connected')
except mp.TimeoutError as err:
    print('timeout')
