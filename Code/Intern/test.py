
import urllib
def internet_on():
    try:
        response=urllib2.urlopen('https://pyzuri.com/',timeout=5)
	check = 1
        return check
    except:		
	check = 0
    	return check
print(internet_on())
