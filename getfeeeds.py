#!/usr/bin/env python3

import feedparser
from urllib.parse import urlparse

feeds = [ 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml',
          'http://rss.cnn.com/rss/cnn_topstories.rss' ]

for url in feeds:
    host = urlparse(url).netloc
    feed = feedparser.parse(url)

    for item in feed['items']:
        print(host + "\t" + item['title'])
