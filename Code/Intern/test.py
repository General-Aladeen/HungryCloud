try:
	response=urllib2.urlopen('https://pyzuri.com/')
	check = 1
except:	
	check = 0
print(check)
