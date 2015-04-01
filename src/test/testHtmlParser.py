'''
Created on Mar 9, 2015

@author: hoavu
'''
import html

url = 'http://www.gannett-cdn.com/-mm-/3bea6f83a1fda721921cc47d327ce4d6d7001442/c=367-0-2166-1799&amp;r=x153&amp;c=150x150/local/-/media/2015/03/08/USATODAY/USATODAY/635614514795625132-USP-NHL--Detroit-Red-Wings-at-Boston-Bruins.jpg'
print (url)
print(html.unescape(url))