'''
Created on Feb 28, 2015

@author: hoavu
'''
import requests
import urllib.parse


normalized_url = 'http://entertainthis.usatoday.com/2015/02/23/shocker-bachelor-chris-narrows-down-to-two/'
clean_url= 'http://saulify.me/clean?u='
clean_url = clean_url + urllib.parse.quote_plus(normalized_url)
article_page = requests.get(clean_url)
print(article_page.text)
