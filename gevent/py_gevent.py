# a library that provides a high-level interface to the event loop
# based on non-blocking IO (libevent/libev) and lightweight greenlets

import gevent
from gevent import monkey

monkey.patch_all()

import requests

def fetch(url):
    return requests.get(url)

urls = ['http://example.com', 'http://example.org', 'http://example.net']
jobs = [gevent.spawn(fetch, url) for url in urls]
gevent.joinall(jobs)

for job in jobs:
    print(job.value.status_code)

# useful in www servers, scraping and serving multiple connections at once
