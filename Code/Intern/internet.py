import urllib
from socket import timeout
#try :
#    stri = "https://www.google.co.in"
#    data = urllib.urlopen(stri,timeout=20)
#    print "Connected"
#except:
#    print "not connected" 
import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('https://www.google.co.in',timeout=1)
        beep = 1
        return beep
    except urllib2.URLError as err:
        beep = 0
        pass
    return beep
print(internet_on())
