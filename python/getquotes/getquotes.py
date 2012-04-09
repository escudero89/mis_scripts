#!/usr/bin/env python

import urllib2, random, string

sub = ["quotations", "attitude", "affirmation", "children", "pchildren", "communication", "energy", "experience", "feedback", "negativity", "reinforcement", "reputation", "sayings", "thinking", "thoughts", "selftalk", "motivational", "motivational3", "motivational4", "motivational5", "motivational6"]

realsub = random.randint(0, len(sub) - 1)

url = 'http://www.positivequotes.org/' + sub[realsub]

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

a = data.split('<div class="quote">')
arandom = random.randint(1, len(a) - 2)

print string.join(a[arandom].split("<span")[0].split()," ").replace("<br>", " ")
