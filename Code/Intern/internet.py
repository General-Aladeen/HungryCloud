import urllib
try :
    stri = "https://www.google.co.in"
    data = urllib.urlopen(stri,timeout=20)
    print "Connected"
except:
    print "not connected" 
