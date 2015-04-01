'''
Created on Feb 6, 2015

@author: hoavu
'''
from model.IIIArticle import IIIArticle
source_id = 'cnn_us'
source_name = 'CNN'


class CNN_Article(IIIArticle):
    
    def __init__(self, url, title, category_id, is_top_story_on_their_site, is_on_home_page, updated_time):
        IIIArticle.__init__(self, url, title, category_id, is_top_story_on_their_site, is_on_home_page, updated_time)
        self.source_id = source_id
    
    
        
        
    