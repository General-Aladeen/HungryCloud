try:
	response=urllib2.urlopen('https://pyzuri.com/',timeout=5)
	check = 1
except:	
	check = 0
print(check)
