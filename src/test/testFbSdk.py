'''
Created on Jun 27, 2015

@author: hoavu
'''
from fbsdk import facebook

 
#FB_LONGLIVE_ACTK=

#FB_LONGLIVE_ACTK="CAAXN0pNpZCdcBALbc7ztRyZBZBk2ZBp6qKExBZAFouRRq9juhCYjfLzOL1aZB8RUIRZAeUXR2VZC537tvwDPgBYkScmunFMXbTHIwgodUJgPbq03tt2KVc9tG8BR0wX65N5iR1ZBdMbEaGRCHlySBP5ZCillgDYxDgCz3Pp9qW7fCaMRSzwrhHUJ8lQ7Oq2T3ZAAYcZD"
#FB_LONGLIVE_ACTK="CAAU0Jjw2opYBAE3SN2BqjtqLz3tzfEuaOecpFz7MiIMCpj3unz4i1b5JX9GsZA3OHFZAZClDOqNXIDP3JvEoswZBPXLEosemRgRbwzTLbN91ae1rjPvBI0M7VEUCTQuGh56CLZAyf1SpMhf5EJPtG4jAeHMRLl0DZC6Lcnwyf1U0xyx6EYDBBZADGcXmE2YW6kZD"
FB_LONGLIVE_ACTK="CAAKPPNabMZBMBAI6ZBVmhdYRGXsQgsw2R4QNmbpJ9DiXBMC6G11ytmeXPMSoZCFcJnd4e6BYkZBKoplnSegkYIdpmDoLQ0T661rmiBrV3QWLvC1nnzFJUPlVFJju2TwsHVIK8x1TeuzETiSLOeSePGYZBEtDHYe4FixhCBVpp5kc7lDqXMquKRtK3TaEB4SMZD"


'''pages_ids = {  '448074378687792', 
  '1446773692292875',
  '1444660152523909',
  '125495547784034',
  '981557541876158',
  '1618314921758229',
  '990065127670512',
  '676771192466399',
  '511637488983898',
  '655674891199022',
  '657642144337270'
 }'''

'''pages_ids = {'1042200592489522',
  '1587055911568155',
  '844151408968031',
  '1009608349063790',
  '1603782689884673',
  '1681255602104922',
  '1596675573936405',
  '1737892323105028',
  '887836154619860',
  '1598864440365293',
 }'''



pages_ids = { '640955502707812',
  '706665812771492',
  '688890877910059',
  '1613359912275169',
  '1610781415865613',
  '404632453067567',
  '452338824945104',
  '1020130411331666',
  '1605650606359891',
  '114003425605040'
 }


def get_api(access_token, page_id):
    graph = facebook.GraphAPI(access_token)
    # Get page token to post as the page. You can skip 
    # the following if you want to post as yourself. 
    resp = graph.get_object('me/accounts?limit=500')
    page_access_token = None
    for page in resp['data']:
        #print( page['id'] + "\t\t" + page['access_token'])
        if page['id'] == page_id:
            page_access_token = page['access_token']
            print(page_id + "    " + page_access_token)
            graph = facebook.GraphAPI(page_access_token)
            return graph
    # You can also skip the above if you get a page token:
    # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
    # and make that long-lived token as in Step 3

for page_id in pages_ids: 
    api = get_api(FB_LONGLIVE_ACTK, page_id)