'''
Created on Feb 26, 2015

@author: hoavu
'''
from fbsdk import facebook


FB_LONGLIVE_ACTK = "CAAUCZBoyBGpUBACo0GuUx75S24R9nzHz8rOPZAXQZBJGzZBKv6dJOjiM2EAbmxKiWZApxQPW0sSlpVAfFu2ZAqzDr5MdbTUxwstdaFWNTbVe4hs68J0NhlPGdN16Fr5BpEZBb9mlxNm7XjQSxARZCos40An5pcVkuUFodWZAQanjJrZCL20xDqyZCmHqaZBdGdgYbHGCBt8c1LqULzjmZA8nL3sNj"
IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'

pages_id = {"657808134330750", '1417094931918673', 
            '329570850574813', '1592315347647071' 
            }

pages_toke = {}
def main():
    # Fill in the values noted in previous steps here
    cfg = {
    "page_id"      : "657808134330750",  # Step 1
    "access_token" : FB_LONGLIVE_ACTK   # Step 3
    }
    
    api = get_api(FB_LONGLIVE_ACTK, '657808134330750')
    msg = "first post link"
    attchment = {"name": "Link name",
             "link": "http://vnexpress.net/photo/giao-thong/doan-duong-500-m-gia-gan-1-000-ty-dong-o-thu-do-3150842.html",
             "caption": "By IIIN",
             "description": "This is a longer description of the attachment",
             "picture": "http://l.f32.img.vnecdn.net/2015/02/26/anh-1-1424922272_660x0.jpg"}
    #print( api.put_wall_post(msg, attachment = attchment)['id'])
    posts = api.get_object(id='657808134330750/feed')
    print(posts['data'])
    for post in posts['data']:
        
        if ('story' in post):
            print("story: " +post['story'])
        if ('message' in post):
            print("story: " +post['message'])
#     print(post['message'])

def get_api(access_token, page_id):
    graph = facebook.GraphAPI(access_token)
    # Get page token to post as the page. You can skip 
    # the following if you want to post as yourself. 
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == page_id:
            page_access_token = page['access_token']
            graph = facebook.GraphAPI(page_access_token)
            return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3
    
def get_api_pagetoken (page_access_token):
    return facebook.GraphAPI(page_access_token)

if __name__ == "__main__":
    main()
    
