import urllib,urllib2
from bs4 import BeautifulSoup  as b4

def get_url():
    base_url = 'https://www.runoob.com/'
    f = open('url.txt', 'w')
    extra = open('extra.txt', 'w')
    n1 = 0
    n2 = 0
    main_req = urllib2.urlopen(urllib2.Request(base_url))
    main_soup =  b4(main_req.read(), 'html.parser')
    for main_http in main_soup.findAll(name='a', attrs={'class':'item-top item-1'}):
        http_url = "https:" + main_http.get("href")
        req = urllib2.Request(http_url)
        reponse = urllib2.urlopen(req)
        soup = b4(reponse.read(), 'html.parser')
        soup = soup.find(name='div', attrs={'id':'leftcolumn'})
        for i in soup.findAll(name='a',attrs = {'target':'_top'}):
            if i.get('href').startswith('/'):
                http = base_url+i.get('href')[1:]
                try:
                    url = urllib2.urlopen(http,timeout=5)
                    code = url.getcode()
                    if code == 200:
                        f.write(http +'\n')
                        n1+=1
                        print n1, http
                except:
                    pass
            else:
                extra.write(base_url+i.get('href')+'\n')
                n2+=1
    f.close()
    extra.close()
    print n2,n1
    #5078
get_url()