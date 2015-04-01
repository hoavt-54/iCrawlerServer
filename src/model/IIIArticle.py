'''
Created on 5 Feb, 2015

@author: Vu Trong Hoa
'''

class IIIArticle:
    def get_title(self):
        raise NotImplementedError( "All article should implement this" )
    
    def __init__(self, url, title, category_id, is_top_story_on_their_site, is_on_home_page, updated_time):
        self.url = url
        self.title = title
        self.category_id = category_id
        self.is_top_story_on_their_site = is_top_story_on_their_site
        self.is_on_home_page = is_on_home_page
        self.updated_time = updated_time
        
    