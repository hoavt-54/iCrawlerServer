'''
Created on Feb 28, 2015

@author: hoavu
'''
from newspaper.article import Article


url = 'http://www.huffingtonpost.com/2015/02/27/jennifer-lawrence-david-o-russell_n_6772866.html'
article = Article(url)
article.download()
article.parse()
#print(article.html)
print(article.text)

