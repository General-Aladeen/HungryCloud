import urllib
try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri,timeout=5)
    print "Connected"
except:
    print "not connected" 
