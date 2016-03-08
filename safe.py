import urllib

class Safe:
    url = "https://sb-ssl.google.com/safebrowsing/api/lookup?"
    params = urllib.urlencode({'client':'nhcert', 'key':'AIzaSyAnrSFUn7ISPQdY6tKPNhCWFNKWX59gbsw', 'appver':'1.5.2', 'pver':'3.1'})
    rcode = []

    def request(self, test):
        test = urllib.quote(test)
        f = urllib.urlopen(self.url + self.params + '&url=' + test)
        self.rcode = f.getcode()
        if self.rcode == 204:
            print "SAFE"
        else:
            print f.read()
    
