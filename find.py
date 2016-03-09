import urllib2
import urllib
from bs4 import BeautifulSoup
import datetime
import pickle
import time

class Safe():
    html = []
    dic = {}
    api_url = "https://sb-ssl.google.com/safebrowsing/api/lookup?"
    param_dic = {'client':'nhcert', 'key':'AIzaSyAnrSFUn7ISPQdY6tKPNhCWFNKWX59gbsw', \
                 'appver':'1.5.2', 'pver':'3.1'}
    api_object = []
    rcode = []
    
    def request(self, start):
        # Request site information.
        req = urllib2.Request('https://search.naver.com/search.naver?' + \
                              'display=10&doc_sources=&ie=utf8&nso=so%3Ar&qdt=&query=%EB%86%8D%ED%98%91&' + \
                              'qvt=&sm=tab_pge&sort=1&source=0&srcharea=1&start={0}&where=site'.format(start))
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0')
        f = urllib2.urlopen(req)
        self.html = f.read()

    def parse(self):
        # Parsing HTML code to find name and URL then store as dic.
        if not self.html:
            print '[*] There are no html.'
            return
        else:
            soup = BeautifulSoup(self.html, 'html.parser')
            for i in soup.find_all('dt'):
                if i.a:
                    self.dic[i.a.get_text()] = i.a.get('href')

    def google_api(self, test):
        # Get API Information.

        try:
            test = urllib.quote(test)
            params = urllib.urlencode(self.param_dic) 
            self.api_object = urllib.urlopen(self.api_url + params + '&url=' + test)
            self.rcode = self.api_object.getcode() 
        except:
            pass

    def save(self):
        # Save site Information.
        d = datetime.date.today()
        name = d.isoformat()

        f = open(name, 'wb')
        pickle.dump(self.dic, f)
        f.close()

def run():
    a = Safe()

#    for i in range(1, 1000, 10):
#        a.request(i)
#        a.parse()
#
#    a.save()

    f = open('2016-03-08')
    a.dic = pickle.load(f)

    b = time.time()

    for c, i in enumerate(a.dic):
        a.google_api(a.dic[i])
        if a.rcode == 204:
            print c, i, '\t\t\t', 'SAFE'
        else:
            print c, i, '\t\t\t', a.api_object.read()

    c = time.time()
    d = c - b
    print '[*] time : %d sec.' % d

if __name__ == '__main__':
    run()

