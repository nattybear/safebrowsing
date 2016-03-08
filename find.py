import urllib2
from bs4 import BeautifulSoup

class Safe():
    html = []
    
    def request(self, start):
        req = urllib2.Request('https://search.naver.com/search.naver?' + \
                              'display=10&doc_sources=&ie=utf8&nso=so%3Ar&qdt=&query=%EB%86%8D%ED%98%91&' + \
                              'qvt=&sm=tab_pge&sort=1&source=0&srcharea=1&start={0}&where=site'.format(start))
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:44.0) Gecko/20100101 Firefox/44.0')
        f = urllib2.urlopen(req)
        self.html = f.read()


