'''
Created on Feb 8, 2015

@author: hoavu
'''
import json
import requests
import urllib.parse
from urllib3 import PoolManager


API = 'http://api.facebook.com/restserver.php'
TWITTER_API = 'http://urls.api.twitter.com/1/urls/count.json'

article_url = 'http://stylenews.peoplestylewatch.com/2015/03/13/jazz-jennings-clean-and-clear-video/'
article_url = urllib.parse.quote(article_url, safe='')
param = dict(
              method = 'links.getStats',
          urls = article_url,
          format = 'json'
          )
tw_param = dict(url=article_url)
# r = PoolManager().request('GET', '')
# print(r.status)
# content = loads(r.json())
# print(content)
#content = loads(urlopen('http://graph.facebook.com/2439131959').read())
resp = requests.get(url=API, params = param)
data = json.loads(resp.text)
print(data)
print(data[0]["comments_fbid"])
twi_resp = requests.get(url=TWITTER_API, params = tw_param)
data = json.loads(twi_resp.text)
print(data)
