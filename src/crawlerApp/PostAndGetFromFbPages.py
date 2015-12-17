'''
Created on Feb 25, 2015

@author: hoavu
'''
import json
import requests
import sys, os
from threading import Thread
from time import sleep
import urllib.parse

from fbsdk import facebook
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection


sys.path.append(os.path.realpath('..'))



IIIN_SERVER_APP_ID="1410650005904021"
IIIN_SERVER_SERCRET = '52c5ce6ee56af4221c6215f3fc1418d4'
FB_REST_API = 'http://api.facebook.com/restserver.php'
TWITTER_URL_API = 'http://urls.api.twitter.com/1/urls/count.json'
POISON = "quite_queue"
'''=========================================================================
Thread waiting to get comment like and share for url, then save result in db
==========================================================================='''
class CommentLikeShrareGetterThread(Thread):
    # define a constructor, parameterised a queue
    def __init__(self, queue):
        Thread.__init__(self)
        self.name= "Thread_share_like_comment_count"
        self.queue = queue;
        self.is_running = True
    
    def stop_running (self):
        self.is_running = False
    
    def run(self):
        
        try:
            db_thread = IIIDatbaseConnection()
            db_thread.init_database_cont()
            next_url = None
            while self.is_running:
                #get statistic on FB, TW
                try:
                    next_url = self.queue.get(True)
                    if (next_url == None or next_url == POISON):
                        self.stop_running()
                        break
                    if (not db_thread.should_update_statisics(next_url)):
                        continue
                    param_url = next_url
                    if ("http://espn.go.com/" in next_url):
                        try:
                            param_url = next_url.split("_/id/")[0] + "_/id/" +  next_url.split("_/id/")[1].split("/")[0];
                        except Exception as e: 
                            print("cannot split espn url")
                            param_url = next_url
                    fb_param = dict(method = 'links.getStats',
                                urls = urllib.parse.quote(param_url, safe=''),
                                format = 'json')
                    
                    #tw_param = dict(url=next_url)
                    fb_resp = requests.get(url=FB_REST_API, params = fb_param)
                    data = json.loads(fb_resp.text)[0]
                    #tw_resp = requests.get(url=TWITTER_URL_API, params = tw_param)
                    #twi_data = json.loads(tw_resp.text)
                    #print(data)
                    #print(twi_data)
                    print(db_thread.update_article_count(next_url, data['comment_count'],
                                                         data['share_count'], data['like_count'], data['comments_fbid'], 0))
                except Exception as e:
                    print("Error when get FB, TW like comment: {}".format(e))

        except Exception as db_e:
            print("Error database thread get like_share count: {}".format(db_e))
        finally:
            #close connection db before exit
            if (db_thread is not None):
                db_thread.close_database_cont()
        print("commentlikeshare thread stoppped")
'''    
=========================== end of get like, share thread =====================
'''    
                    
                    
                    
                    
                    
                    
                    
source_fb_photo = ['bleacherreport_us', 'espn_usa',
                   'cbs_news', 'nbc_news', 'business_insider',
                   'bloomberg', 'forbes_usa', 'mashable',
                   'buzzfeed', 'uproxx', 'theblaze', 
                   'washington_post', 'abc_news', 
                   'eonline_us', 'fox_news', 'la_times',
                   'iflscience', 'nydailynews', 'reuters',
                   'cnbc']                    


# tokenapp1=
pages_ids1 = ['1604389706488219', '907078942662563',
              '489084041252278', '840846699361685',
              '1084403788266752', '547770868705066',
              
 ]

pages_token1 = ['CAAL5K86srZC4BADj5nGMgTuxydzSt1qlQzwIlLYakYkJZB3MuDa7XYxZBex6avTtsVKh59djW8Ks0RD0ubGYVl8ykQbbOhIFAAZBrZCjj5iUQv40jcVK8PkACRbR1ojNonQQHUz6i41oDFj0mG1oarTpXLEObwdRt6ws6x5bd6Vcs8Ny9JTAZB',
                'CAAL5K86srZC4BAGqErW0GjZBVtOWANzx5jQvUbii78ps4lBKKIKHNMo1KnLXG5TiITap1ALhYicREcCh5Q4GqyXZCqe2LfYG026fA38tYUdVObuZCCLikewpl0xgznKWceoC0if9HfhXm5Ey0cs0auPe8UyNQ4k11RwgRTCwZAUOijICRttJqcFKLBRfyChMZD',
                'CAAL5K86srZC4BAJFzA1i8YEZBIGuV3Ub3csYZBgpFUKDsOiaqVsIu6K1K29ZB4Ryt6NT9R82uC1pf1ds7nFQyp4QLFapJUoPhZAZCZCGWuDaj3AEsZAJseFCzpm1ZA5KArTzksJhZAsbnB0WHzx999dpWP2Ywmy0MhEZBkjnMNhDXR96hpUEIM6ek2Y',
                'CAAL5K86srZC4BABu3uWzo0lWyGgZBy73sshswWnDvjZARZAbqD1ZBeQWCpUB7EpFjALOUEOqoL5Xq5YlHyOOuqDZAECaY3hZAzR40htxFRSP14u6ncZCmsxjP9YsvncCGs23eXK6kLgtRScuZCvRfR6lwpngVDGl0ZAFm2crDou5D1OY8YZC9XD2f5qmYDbZAkdS1gMZD',
                'CAAL5K86srZC4BAMASe5VkwRls0Xl81aI1nAmd5pWf9oLJJY5L1dZCQRyFBlaRQUviCB3FcWpls5w13BgOe4g6L7z79reYHnWVM7bcj2XZA8PipYw4WyC90eN1UFLZBcH24PhHp8rOtuBZAH0wb7oAcsowcOKPiLZCGF7R0YNe7jZBSxypSQpegr',
                'CAAL5K86srZC4BAEG9xvS8lCdmdU6p59B6dUVbeFPVXkC7qSwBXBv30qDNhL33ZBLJUKAKVVvrAPXakRShoOU81eFEVfy1cDZCpz4tWAUY2qHJQ2TpVBblIqZCRYgnX681JcpEDzqaAxwEal3M7VlwnxRABSmghjqbIFUvc6xR3pdjRBi7dZBL'
                ]


pages_ids2= ['417943228400813', '904404192971405',
              '1056770051022165', '1482782695384829',
              '1644567635796236', '1634740096775651',]
pages_tokens2 = ['CAAL5K86srZC4BAP9oZA0f2JEJtAKEDqZAKfZCVi5ZAkoLU8ZBplhlOyqtTCG9y8EkzqYr4Niog79VRB7XXfHQkdqasHpBUBkU7TiNZADdzwju0ZCSZAIQuYu3y3jBVZBXUMAxbWEg8a0A0SOgjQ76XrUt1RhoZCCUUPweSbBU7b5EwDr6mQU8pffvMZA',
                'CAAL5K86srZC4BAMgEsdd1iq0YOCZCZApC0SMXY86Q8YTHkZCWS25Jbl4NJpqg3VC5S54Th2YJItZCyJ0iv91TOEZBiaZAZB6So6lYyl8ZBwyQvPFlunuuZCdOuVFZCBGF21AZBQyOeD6ZAoW3HBKt4o4xE8Eamc9SBvbyU6fRjITz28a9YGB2JhenYjlAimERs0s9ShUZD',
                'CAAL5K86srZC4BAAsYwWbruHAaJ8hiWiezu2XEdjyY5gOBMZCUHoL6ZCZC1R2TzdYiLBZBtDlNd8Yb6SVtqkoWfntIEZAv9HgGAay7CtrbhZBBwbZCmWg4VBEQkVJRqTayiEqDYMlhX7To1zZBxMNDEjfhqLdRThkW5qhjXDpD6bwZA5x4D2sS5IU3eFOmXK1h8vTQZD',
                'CAAL5K86srZC4BAKJD2fR6WGNG9LEhDf1jAp8hyeiVAlD4fZAha2uIoN1L11QyONLhtdUinA30mktY9sFu9ciquRGX78SuAdWkdRpf4eOSG3iAfZCk7ZAjw3xqHvZBt37po5Pyzzjs8ZAQ4ZB8H3A77TieZBGV36dTQzFbZAjZCigZBmFFyD5nxva8nOJyLfXv8csu4ZD',
                'CAAL5K86srZC4BAPzqIJHLlF7avwFVOQ4FGpk8XBk2Kx7D2lIG8zpSrx7H92NmVdSBqFgZAvKY4KZCion2ZBUGxmHv4mDLfJUlqdNMKTq5iFRsakzUvRRbNMQPlECwnZBMEKfZASKTjXZAZAsDYn7ZC2Kj387dSQjtB4P0gvXAMPgoq5Vip0NS5TVLIP4PGhIuNRoZD',
                'CAAL5K86srZC4BAPquAHCxXRk4lJ27jUCb9EzITJF5QJPeroeP67BK0ZBAU7p3HTEfoySAPQc1sau6DMGPxSldzAyzw5NFZCg7WBdJfvs3s6H8uDMlh2w78tyL0NZAzI8JZBR7TgBDPzksXvNturZARnZCIP7yUMSxdvO6TJyDjsEjcAF8KegyDD'                 
                 ]

pages_ids3= ['1394037944249687', '182866568713609',
             '834979589954156', '445841905563902',
             '832134960232457', '879948208767161'
             ]
pages_tokens3 = ['CAAFZBdv4f2QoBAIMtiX0SWSMzn1C43nj1f9ZAyLFPKRBZAjKjcLro3OaOgHujrS9EDzQjtaZB60LpjdNkZBms2w8jgWWplouIo0xabnkWM1NVX3ee361UEG7r4LL5zuFfOEyPUBOlztj3e7RY9ubBVzcm8CLAwQSmdTETumJAYhC30uuBo7g1',
                 'CAAFZBdv4f2QoBAPYQmVpmejDHUxWniBsApRMR7cQ1cXffTTmuY9rBmsxFxJPZAZB0TGhm429bJZAzQ6RhVARpJWELDqo3hmnuDZBXHeRFZAWJkwVpZAZArUS0t5MgCRUV1LDZB4Bb5lxOVWNy06orGfJRfkj42aLIzH41HJQevpLZCoKo1bRXJNRVM',
                 'CAAFZBdv4f2QoBAKLg37qW3T4PWZBaj7UKPocM5xwVrSy0j6ZAWqebsTSlKkikWO2OP8ZCk5TwJaSZBlBojagRG5eNiS8hEY41f9mDb0vslHRp7DOkRFrmwOlrA0EnXSIIYGiuLhLczO1U0h6bxb2kUpNYkR5AvxOKDiQKrrZCIepPG3jt8xFCm',
                 'CAAFZBdv4f2QoBAMtOQKdKlqiUag6VHc8lXaeCw3Hui9dPKj0edSDyEoQPZBrWO9ZCBpnNAnU7OZA8FUZA83FkFyRCZCZBVSPjEqT4h4e60XUYyE4BJ1C8aPFdwInA8LD8ollOVCT8enUvcO2rqu4NiqreavuksU8q0PmWKQIkdH4blt2UoAAGBo',
                 'CAAFZBdv4f2QoBAK6V7LZCh8nyKkAtzWX3XdrIr20ZA28wStZBnGw1OdE5KYY66ESclzbIXN0FvrdyPPt5LXwilKf1lXcdbMHZCeh5EauGlx7JKEw366rRkDeDD0WVxgotXdc8XQ7X2p5giHq1DU1SO2CTjBCX4tyRTPQLi8NuZC5Ay06fKcSgYAqXPVq0WNk8ZD',
                 'CAAFZBdv4f2QoBAM5iH3J2jPPovXlhfZCNrGqJJQCCqXrzkn9IdGO4VharbhLvUvkYt0bUO6KlccaAFn02xU0C4KNQDgRXTjKj02SJg3AJVIYhBElVl6ZBI7aFLIIDGpil3PieVZCyk4yOACfR0yTPBe8hZCxgIF71vyESeiGHsdVY6WAROnlaGcCW87pElQYZD'
                 ]
pages_ids4=['329570850574813', '1063513427002614',
            '1388104431490931', '1588155624772622',
            '529885843825598', '935700969834561'
            ]
pages_tokens4 = ['CAAFZBdv4f2QoBABoOcIvyiEpWq2ZBpZAgvKNUzoxZBlyUwsJZAXW3LveXs87kB7jdDaxE4daCDmxngQXfN0cAf1CZCYM6UmfHHDInuaQ14c1PNQWBWTW35WmVqEPcjxZBSTCZCZC6GL7MwgQR4OLAPe6V37Ya9vAVh8wvYpuxvQskdKVNUtsJ8wxq7Lebr1aiKWMZD',
                 'CAAFZBdv4f2QoBAEjvPAafVQqL9XfIcT6vdo9VeCyw7S1yzZAOqmIv4RHJfdKZCJmn1kgIW2DO5QZCNbjtN0ZANCxXvWZBkZBvWcFARlJAwSKXh604177ULXQZBHeNshg7aEB9hYnOiNVswyF71xpxIbAfkQ8uEgxojNuGDflATZAFAZBIklSMlyU8y',
                 'CAAFZBdv4f2QoBALpzHbmRX4pkdA82PuO9MLM7BajBWpv2eZCTZBmvZBf6MCukNZBGArgfajF1OhZBtnGPkJ9K7r8OtZCgZCaThP3nZCyUKPEkMWbA0QZBZCZAewbuYpr8WUUm925CXVZCOpZBy6INGLtyaWZBV57vKQqbKjMFDCC7kY4rqzjLCryEcZBwoFjEvfJU81ZCoBQZD',
                 'CAAFZBdv4f2QoBABbyMeIKrf3BeW0UmQHvqAxonK6veaoCYI52kZCZBk2ZCDqIZCKalJv40IuelBgE8SzoxANZAuOMVYX6ZBkBFIaeEiHjHH3TDeHBU27X9KLWo1zad8d7n3Qs9TNIXE1rEeQb5agN0n7JH1T7MkDj4QqpE4YDc8NUyVOgLeQGMjNdYldW8YRZCEZD',
                 'CAAFZBdv4f2QoBAIlDEZCSNbRyAZCThZCwZBxBR6S8RouuUmWgE1fQt2dghu4czFzrOvKaepRzAe20WpZCpzZBbD7RvxQ1sXyZBvvlr6S4VCKVd0zUZAknmVyJem896xg6lhOFlReDxGE71UUGcRBcJomzZBXjBB9twszcxk1owWxRpq49IO25XgZAEgyN9ft5NmBBwZD',
                 'CAAFZBdv4f2QoBAPdCxULbc08sFsBckOE5K4ZA0gqz50wznaH2ZCmb9GX1TwlQbE6ZAmOPzDrqgxRt4Q2eEla7a09I4bJjk3PttlZC5ZC08bucQoZClYIfijidHROQcWc9f7xxtpezwerZCGJwMbvZBpMu2CtUazzjN7TvsccMsIgbMomdnPSnIhxS',
                 ]
pages_ids5 = ['508334185999807', '880828675311080',
              '894533423929042', '592177567585710',
              '388362948009298', '412027802330139']

pages_token5 = ['CAAGdllFZCZCDwBAI6iM2R2ZB796wpNNv1XtnGLUDywGEHMRfUKmeDOfJzl7AJggBBTUCa4ZCfj70rUfIrgJSl9S7gr5awMOEHAwoW3dQUBihgCrLUaIr5xIDg3qizqSA2caHa2KeUkQj0T1FHC5MAiuLoEtLvQYjNKZBZBJZASKZBvGs9y2QLApFsZBCGAwqa79EZD',
                'CAAGdllFZCZCDwBACgPrLinreDlVtfQgCdHzM4Wk9bHngRKOZC4aBOueKMzvfGtPQjXnEkWVqZBvmQUYGyuk7v4Eq9kZCf7mIq7ZCVZAPFHtgM5xYCFRpQ9hseeFHTYzFj2KY1Yz8MQBmhMsR7zZAMp4kKF4NeJ88ZCwrDgcsMO1xXJ461auoeyZCPtgj5LkwsaoMQZD',
                'CAAGdllFZCZCDwBAE9fZBSjCJyv3wovkefNgAZBdVGmoIbfE1nSKdLX40GhoZAA7jDARzANgaeXlROZBZAMTpdWVUlr06icw6psZCZBtoZBzwU4DkMArnwMkLpvVJdK3eyCLzZC23UhGtRwFPni2FHDxOXHp9jNkLYNQrLeEUaY4kU2tsaPHwiZAOyJap0VTWPAVPTWAZD',
                'CAAGdllFZCZCDwBALSWRjltyXqR7z6F3qzswAZBTToSR2EbfMgpL9DOZBeuOJStu0zoq6o8liMn0bYiyr6Q8DL3pxko4IzhiupNRE0VPQdZBjcTn2b6Cdlq78iZBzfZCeTZAUmHMldurV9QWKKd66dmZBuMVZCgSLxvYbTsxhcVSmN5WJDW8fTsh0u7BDRV137ZBVycZD',
                'CAAGdllFZCZCDwBAI1ZBDWWdAozeBZA8ih5Nc9rQRssBOpHH3n1iOmJu7HUtjs27e8tVIbMj8gXoDffPwt541J1mowDxu70xZBWHLru0UHzztY4gZCZCbekAWwREivwQt5FUnVuhNI3Sp2lNEGWGlPbQDCOH4zeGRB3fUFqF55Yr9JWPrDfZBGWyC',
                'CAAGdllFZCZCDwBAMYQgYXQxzZCjsUg3DFSzG6c9z9CzhOFCHmGZA2F92tbLG6CZA4saYlvzknaJnbZBnOA4TXPTV16GWMfv7HiXsuJRDLR4wqFQdJAztsHJfYFhcyUVmLw8OuLMqEzJm6Jw8P2nJi0FL0rM97cHgJrDFWCzh9EDU0jCN2JZCwFT',
                ]

pages_id6 =['102975006707199', '778046915618571',
            '1571382756463440', '947318508684463',
            '414583335389044', '448888235305944'
            ]
pages_tokens6=['CAAGdllFZCZCDwBAI1QfKHRDEVHfG4QdK8zwueVkf9NbNvilWP2ETofS3ZBOTkc8Nnm4TRQtMwb4RSev3ZBRdSYOAZAqIph9cSMjXS7hknZBnetiKBpWWiE0SuxHkOBLmZCRBXW2byQxkAZBe8dIsKtwkXOTFow1NQ5LywJCJllIV0O36Ab9yFcNy1GgvCSoSjrEZD',
               'CAAGdllFZCZCDwBADwZAnSdWVJPzai390ZAgMvTgiD5BAvPJhZBHiJ4yZBO1itS5BGXx3mkvvnZCWar8xMxHRv2goWfuJUVjcQK6wd6yBNC4DEQEVV15dRLstagevPzyA0hEbjOmvJgkZA7kG5FMfccziTixSStIDHGT0hdrRqQEgt7hzTjB8utK8ssDlA5XOiXoZD',
               'CAAGdllFZCZCDwBAJRXRwEL0GdAc92rmpo4AQLJfGsVYjf73gQnQZByb1hfWTYaIHjFaz9UhfIPNEOFJ2WRbaYHSWdpaVZA4r3wHtTM9gZAzlDidVldBbsIqctf2JiT6vCfJmYuLdtAsQiEC0LhxMCUPVClwgMrUK5DMYnaWfETkXUNHg1AJ1Iq0oOCbaS9CIZD',
               'CAAGdllFZCZCDwBABa9qi5WXhKbuusKeQNoZBQi6zucZBex9cAThyWfRPfTjsGRZAN7P3Ukck2Brvt37rjdTWJ7AYG9Iz9k6k7s6sUWOvXeZCNtDL0dRCU6cIThNZCCMZC3SiBiCTLNgZC9gnj5bV8JCBVT9GgmZAL2FdGkbgqI1wZCKEihYHRioozRi',
               'CAAGdllFZCZCDwBAJ5pnnqPMhTjwn9mZB7QDUXyMrWFlQ7yqPNx8X1iu2hE8mnHCTIEenZByR5qHQrB5EM8Y4ZBrJ78MupNZA4oni9vuG05TvcTj3ptIlJIGB638Nd561qTFhWkEPbYweDSDEIFfux7o6V7zZBPSS9FFpZBEpOyB9vejXo3hiFdUyqqcXyUCqXlUZD',
               'CAAGdllFZCZCDwBANXZC81W29XQNLk7I0CrNE4C37kZAYi8bNPqunZBdT6NO0CUNKyT1E7uISZBQiaE98MqJrW6gezgQ6ZAZBuYh0uyh4aVtJhQMeQ66GrOxsUdEKEvSv3rwQw5xqZCan56rTD0kMazfEJMX0qA6vvemrB0sEfTq9Y3QqP7xyLPeEjNSZCmOSWJDdYZD'
               ]



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

def get_api_pagetoken (self, page_access_token):
    return facebook.GraphAPI(page_access_token)

                    
class PostToFacebookPage(Thread):
    
    # define a constructor, parameterised a queue
    def __init__(self, queue, ids, tokens):
        Thread.__init__(self)
        self.name= "Thread_post_2_facebook_page"
        self.queue = queue;
        self.tokens = tokens
        self.ids = ids
        self.is_running = True
        self.FB_LONGLIVE_ACTK = None
        self.LAST_TIME_GET_TOKEN = 0
    
    def stop_running (self):
        self.is_running = False
        
    def run(self):
        print("thread post article to page already started")
        try:
            db_thread = None
            next_article = None
            count = 0
            #get statistic on FB, TW
            while self.is_running:
                try:
                    next_article = self.queue.get(True)
                    ''' sometime post bloomberg image causing error: (#100) picture URL is not properly formatted '''
                    if (POISON == next_article):
                        self.stop_running()
                        break
                    if ( next_article.thumbnail_url is None or len(next_article.thumbnail_url) < 8):#''''bloomberg' in next_article.url or'''
                        continue
                    if (next_article.thumbnail_url.startswith("//")):
                        next_article.thumbnail_url = "http:" + next_article.thumbnail_url
                        
                    '''put photo to fb'''
                    result_photo = None
                    result_photo_urls = None
                    tk_index = -1
                    try:
                        count = count + 1
                        tk_index= count % len(self.tokens)
                        api = facebook.GraphAPI(self.tokens[tk_index])
                        result_photo =  api.put_photo_url_2_page(next_article.short_description, next_article.thumbnail_url, profile_id="me", published=False)
                        post = api.get_object(id=result_photo['id'], fields="images")
                        result_photo_urls = str(post['images'])
                        print("photo_Id: " + result_photo['id'])
                        #print("result_photo_urls: " + str(result_photo_urls))
                    except Exception as e:
                        #print("Error index: " + tk_index)
                        print("Cannot post photo " + next_article.thumbnail_url + " to FB page {}".format(e))
                        
                    if ((result_photo is None or result_photo['id'] is None)):
                        print("Cannot post " + next_article.url + " to FB page")
                    else: # save id to database
                        '''save db post id'''
                        try:
                            try:
                                db_thread = IIIDatbaseConnection()
                                db_thread.init_database_cont()
                                print("update fb thumnail database result: ")
                                print(db_thread.update_article_fbid_photo(next_article.url, result_photo_urls, result_photo['id'] if result_photo is not None else None))
                            finally:
                                db_thread.close_database_cont()
                        except Exception as e:
                            print("Error save FB id to database: {}".format(e))
                        
                except Exception as e:
                    print("Error when post article to FB pages: {}".format(e))
                sleep(0.8)
            print("thread post article to FB stopped")
        except Exception as db_e:
            print("Error database thread post to Facebook: {}".format(db_e))
    
    