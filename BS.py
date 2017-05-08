Skip to content
Features Business Explore Pricing
This repository
Search
Sign in or Sign up
 Watch 1  Star 1  Fork 0 leportella/tutorials
 Code  Issues 0  Pull requests 0  Projects 0  Pulse  Graphs
Branch: master Find file Copy pathtutorials/scrapping/rotamarinha_v1_BeautifulSoup/scrap_urls.py
7048b56  on 14 May 2016
@leportella leportella scrapy testes
1 contributor
RawBlameHistory     
38 lines (29 sloc)  901 Bytes
#!/usr/bin/python
# -*- coding: utf-8 -*-

#For Python 2.7

import urllib2
from BeautifulSoup import BeautifulSoup


def FindLinks(url, class_name, url_keyword=None):
    url = url
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    data = soup.findAll('div',attrs={'class':class_name})

    links=[]
    for div in data:
        Tag_a = div.findAll('a')
        for a in Tag_a:
            temp = a['href'].split('/')
            if url_keyword:
                for i in temp:
                    if i==url_keyword:
                        links.append(a['href'])
            else:
                links.append(a['href'])
    return links
    
def FindArticles(url):
    url = url
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    data = soup.findAll('div',attrs={'property':'rnews:articleBody'})
    textopuro = data[0].getText()
    return textopuro


Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help