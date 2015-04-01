'''
Created on 4 Feb, 2015

@author: Vu Trong Hoa
'''
from pymysql.err import MySQLError

#from DatabaseConnectionLib import IIIDatbaseConnection
from iiidatabase.DatabaseConnectionLib import IIIDatbaseConnection
cnn_category = {    'sport' : 'sport',
                    'world' : 'world',
                    'tech' : 'tech',
                    'entertainment' : 'entertainment',
                    'opinions' : 'opinions',
                    'more' : 'others'
                }
try:
    db_connect = IIIDatbaseConnection()
    db_connect.init_database_cont()
    #start query everything here
    #print(db_connect.insert_category('category3', 'Category3'))   
#     print(db_connect.insert_source('usa_today', 'USA Today', 'http://www.usatoday.com'))
    #print(db_connect.insert_source2('vnexpress', 'VNEpress', 'http://vnexpress.net','http://graph.facebook.com/612208245488345/picture?type=large'))
    print(db_connect.insert_source2('huffington_usa', 'The Huffington Post', 'http://www.huffingtonpost.com/','graph.facebook.com/18468761129/picture?type=large'))
    #print(db_connect.insert_article('http://this_is_first_bbc_url', 'this is funny article', 
    #                             '43252', 'bbc_uk', 'entertainment', 10, 10, 10, True, False))
    
    #print(db_connect.update_article_like('http://this_is_first_bbc_url', 100))
    #print(db_connect.is_url_existed('http://this_is_first_bbc_urldf'))
#     print(db_connect.insert_category('sport', 'Sport'))
#     print(db_connect.insert_category('world', 'World'))
#     print(db_connect.insert_category('tech', 'Technology'))
#     print(db_connect.insert_category('entertainment', 'Entertainment'))
#     print(db_connect.insert_category('opinions', 'Opinions'))
#     print(db_connect.insert_category('style', 'Style'))
#     print(db_connect.insert_category('politics', 'Politics'))
#     print(db_connect.insert_category('health', 'Health'))
#     print(db_connect.insert_category('news', 'News'))
#     print(db_connect.insert_category('education', 'Education'))
#     print(db_connect.insert_category('law', 'Law'))
#     print(db_connect.insert_category('community', 'Community'))
    #print(db_connect.insert_article2("edition.cnn.com/2015/02/06/world/gallery/week-in-photos-0206/index.html", 
    #                                 "Could a robot have written this story? The rise of the Robo-journalist - CNN.com", 
    #                                 'cnn_usa', 'sport', False, False, 1423267200, 
    #                                 'http://i2.cdn.turner.com/cnnnext/dam/assets/150204142825-459229772-large-169.jpg', 
    #                                 'Advancements in programming and artificial intelligence are creating "bots" that can write copy good enough to pass the scrutiny of a human reader'))
    
    #print(db_connect.update_article_hotpoint('http://this_is_first_bbc_url', 0.8))
    #db_connect.delete_category('category2')
    #
    db_connect.close_database_cont()
except MySQLError as e:
    print('Something went wrong: {}'.format(e))