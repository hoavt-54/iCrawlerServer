'''
Created on Feb 24, 2015

@author: hoavu
'''
from collections import Counter
import nltk
import re, math
import requests
import urllib.parse
from urllib.request import urlopen
from nltk.stem.porter import PorterStemmer
import sys,os
sys.path.append(os.path.realpath('..'))
vn_date_dict = {'Thứ sáu' : 'Friday', 'Thứ ba': 'Tuesday',
                'Thứ tư' : 'Wednesday', 'Thứ năm' : 'Thursday',
                 'Thứ hai' : 'Monday' , 'Thứ bảy' : 'Saturday',
                 'Chủ nhật' : 'Sunday'}

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def normalize_url (url):
    url = url.split("?")[0].split("#")[0];
    print('url before open: ' + url)
    resp = urlopen(url)
    return resp.url.split("?")[0].split("#")[0];

def convert_vn_date (vn_date):
    for key in vn_date_dict:
        vn_date = vn_date.replace(key, vn_date_dict[key])
    return vn_date

def get_text_html_saulify (url):
    clean_url = 'http://saulify.me/clean?u='
    clean_url = clean_url + urllib.parse.quote_plus(url)
    article_page = requests.get(clean_url)
    return article_page.text

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def get_consine_text (text1, text2):
    if (len(text1) < 500 or len(text2) < 500):
        return 0
    return get_cosine(text_to_vector(text1), text_to_vector(text2))
def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)
def normalize_text (text):
    lmtzr = PorterStemmer()
    '''plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
               'died', 'agreed', 'owned', 'humbled', 'sized',
               'meeting', 'stating', 'siezing', 'itemization',
               'sensational', 'traditional', 'reference', 'colonizer',
               'plotted']
    singles = []
    for plural in plurals:
        singles.append(lmtzr.stem(plural))
    print(singles)'''
        
    normalised_string1 = ""
    with open ("../../stopwords_en.txt", "r") as myfile:
        stopwords=myfile.read().replace('\n', '')
    tokens1 = nltk.word_tokenize(text.lower())
    for word in tokens1:
        if word not in stopwords:
            normalised_string1 +=  lmtzr.stem(word) +" "
    #print("normalised: " +normalised_string1)
    return normalised_string1;

def normalize_text_nostop (text):
    lmtzr = PorterStemmer()
    '''plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
               'died', 'agreed', 'owned', 'humbled', 'sized',
               'meeting', 'stating', 'siezing', 'itemization',
               'sensational', 'traditional', 'reference', 'colonizer',
               'plotted']
    singles = []
    for plural in plurals:
        singles.append(lmtzr.stem(plural))
    print(singles)'''
        
    normalised_string1 = ""
    tokens1 = nltk.word_tokenize(text.lower())
    for word in tokens1:
        normalised_string1 +=  lmtzr.stem(word) +" "
    #print("normalised: " +normalised_string1)
    return normalised_string1;

# def get_text_html_

# url = ' http://cnn.it/1FR64kT'
# print(normalize_url(url))
