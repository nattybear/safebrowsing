import urllib

test = raw_input("URL : ")

url = "https://sb-ssl.google.com/safebrowsing/api/lookup?"

params = urllib.urlencode({'client':'nhcert','key':'AIzaSyAnrSFUn7ISPQdY6tKPNhCWFNKWX59gbsw','appver':'1.5.2','pver':'3.1','url':test})

f = urllib.urlopen(url + params)

rcode = f.getcode()

if rcode == 204:
	print "SAFE"

print f.read()
