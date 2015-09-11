'''
Created on Feb 28, 2015

@author: hoavu
'''

import requests
import urllib.parse
import nltk
from newspaper.article import Article
from crawlerApp.utils import get_cosine, text_to_vector, normalize_text

'''get stop words first '''

with open ("stopwords_en.txt", "r") as myfile:
    stopwords=myfile.read().replace('\n', '')

normalized_url = 'http://www.nytimes.com/2015/05/25/science/john-nash-a-beautiful-mind-subject-and-nobel-winner-dies-at-86.html'
article1 = Article(normalized_url)
article1.download()

""" 0.62 is good threshold"""

normalized_url2 = 'http://abcnews.go.com/US/john-nash-beautiful-mind-mathematician-wife-killed-jersey/story?id=31268512'
article2 = Article(normalized_url2)
article2.download()

print("download finished")

article1.parse()
string1 = article1.text
article2.parse()
string2 = article2.text

normalised_string1 = normalize_text(string1)
normalised_string2 = normalize_text(string2)
print("tokenized finished")

print("stopword finished")
print("")
print("")
print(normalised_string1)
print("")
print("")
print(normalised_string2)
print("")
print("")
vector1 = text_to_vector(normalised_string1)
vector2 = text_to_vector(normalised_string2)
print(vector1)
print(vector2)
print(get_cosine(vector1,vector2 ))
vetor_title1 = text_to_vector(normalize_text("John F. Nash Jr., Math Genius Defined by a ‘Beautiful Mind,’ Dies at 86"))
vetor_title2 = text_to_vector(normalize_text("A Beautiful Mind' Mathematician John Nash and His Wife Killed in New Jersey Taxi Crash"))
print(get_cosine(vetor_title1, vetor_title2))
similarity = (0.7 * get_cosine(vector1,vector2 ) + 0.3 * get_cosine(vetor_title1, vetor_title2))
print(similarity)
