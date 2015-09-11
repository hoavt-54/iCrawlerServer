'''
Created on Apr 14, 2015

@author: hoavu
'''
try:
    from lxml import etree
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")


import requests
from lxml import html
from extractContent.ContentExtractor import ContentExtractor
import re
from apt.progress.text import long
# import os.path
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from crawlerApp.utils import unix_time_to_string
class buzzFeedContentExtractor(ContentExtractor):
    def parse(self, html_tree, title, pub_date, url):
        print("start parsing simple html here")
        self.title = title
        self.pub_date = pub_date
        
        
        ''' Extract author '''
        try:
            author_names = html_tree.xpath('//a[@class="byline__author"]')
            for name in author_names:
                self.author =  self.author + str(name.text + ", ")
            author_title = html_tree.xpath('//div[@class="byline__title"]/text()')[0]
            self.author = self.author + author_title
        except Exception as e:
            print("Error when get author from text {}".format(e))
        try:
            self.author = html_tree.xpath('//meta[@property="author"]')[0].attrib['content']
        except Exception as e2:
            print("Error when get author from meta tag {}".format(e2))
            print("author: ")
        print(self.author)
        
        
        ''' Extract body tag text '''
        body_tag = html_tree.xpath('//div[@id="buzz_sub_buzz"]')[0]
        print_tags = body_tag.xpath('//p[@class="print"]')#remove some "view this image" text
        for tag in print_tags:
            tag.getparent().remove(tag)
        print_tags = body_tag.xpath('//span[@class="print"]')#remove some "view this video" text
        for tag in print_tags:
            tag.getparent().remove(tag)
        via_tags = body_tag.xpath('//div[@class="sub_buzz_source_via buzz_attribution"]')#remove some "via tag" text
        for tag in via_tags:
            tag.getparent().remove(tag)
            
            
        '''Fix img tag abit '''# seem to be no need
        img_tags = body_tag.xpath('//img')
        for tag in img_tags:
            src_tag = tag.get('src')
            src_rel_tag = tag.get('rel:bf_image_src')
            if src_tag is not None and str(src_tag).startswith("data:image") and src_rel_tag is not None:
                tag.set('src', src_rel_tag)
            
        ''' Fix tweet  bf, adding twitter-tweet class'''
        tweetblocks = body_tag.xpath('//blockquote[@class="bf-tweet"]')
        for block in tweetblocks:
            block.set('class', 'twitter-tweet bf-tweet')
            
        ''' Fix instagram abit, lack of class '''
        instag_blocks = body_tag.xpath('//blockquote[starts-with(@id,"instagram")]')
        for block in instag_blocks:
            if block.get('class') is None or "instagram-media" not in block.get("class"):
                block.set('class', 'instagram-media')
        
        self.body_tag = etree.tostring(body_tag, method="html" , encoding='unicode') # for now we not remove anything
        
        
        
        







# normalized_url = 'http://www.buzzfeed.com/katherinemiller/charts-lots-of-charts#.mc8GpQ5ME'
# article_page = requests.get(normalized_url)
# title = "What The F**k Is Up With Dental Dams?"
# extractor = buzzFeedContentExtractor()
# extractor.parse(html.fromstring(article_page.text), title, None, normalized_url)
# f = open('htmltext.html','w')
# f.write(extractor.to_html())
