#!/usr/bin/env python

import urllib2, string

url = 'http://www.proverbia.net/google/'

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

a = data.split('<TD CLASS="frasedeldia">')

print a[1].split("</TD>")[0] + a[1].split("<k>")[1].split("</k>")[0].replace("&nbsp;"," ")
