'''
Created on Apr 14, 2015

@author: hoavu
'''
import html as true_html
import os.path
import sys
sys.path.append(os.path.realpath('..'))
unicode_fix = {'â' : "'",
               'â': "-"}  
class ContentExtractor:
    def __init__(self):
        self.title = None
        self.author = ""
        self.pub_date = None
        self.body_tag = ""
        self.url = None
    
    def parse(self):
        print("this method parse all the attributes")
        
    def to_html(self):
        header_part = ""
        ending_part = ""
        with open ("../extractContent/header.txt", "r") as headfile:
            header_part = headfile.read()
        with open ("../extractContent/ending.txt", "r") as endfile:
            ending_part = endfile.read()
        title_part = "<h2> <a href=\"\">" + self.title + "</a></h2>" + "<h4>"  + "By "+ self.author +"</h4>" + "<h4>" + self.pub_date +"</h4>" + "</br>"
        return_string = header_part + title_part + true_html.unescape(str(self.body_tag)) + ending_part
        for wired_string in unicode_fix:
            return_string = return_string.replace(wired_string, unicode_fix.get(wired_string))
        print("parse simple html okay")
        return return_string