import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
import twitter
import io
from collections import Counter
from functools import partial
from sys import maxsize
from outh_login import outh_login
from make_twitter_request import make_twitter_request
from save_json import save_json

## Harvesting a user's tweets 
def harvest_user_timeline(twitter_api, screen_name = None, user_id = None, max_results = 10000):
    assert (screen_name != None) != (user_id !=None) ## Must have screen name or user id , not both
    
    kw = {"count":200, "trim_user":"true", "include_rts":"true", "since_id":1 } ## keyword arguments for Twitter API call
    
    if screen_name:
       kw['screen_name'] = screen_name
    else:
       kw['user_id'] = user_id
        
    max_pages = 16
    
    results = []
    
    tweets = make_twitter_request(twitter_api.statuses.user_timeline, **kw)
    
    if tweets is None:  ## Like in case of Not Authorised 401 errors
       tweets = []
    results += tweets
    
    print(("Fetched %i tweets" % len(tweets)), file=sys.stderr)
    
    page_num = 1
    
    if max_results == kw['count']:
       page_num = max_pages  ## to prevent loop entry
       
    while page_num < max_pages and len(tweets) > 0 and len(results) < max_results:
          kw['max_id'] = min([tweet['id'] for tweet in tweets]) - 1
          tweets = make_twitter_request(twitter_api.statuses.user_timeline, **kw)
          results += tweets
          
          print(("Fetched %i tweets" % len(tweets)), file=sys.stderr) 
          
          page_num += 1
          
    print("Done fetching tweets...", file = sys.stderr)
    print("Total length of tweets fetched", len(results))
    return results[:max_results]
    
if __name__ == '__main__':
        twitter_api = outh_login()
        ##screen_name = "HillaryClinton"
        screen_name ="ABC"
        data = harvest_user_timeline(twitter_api, screen_name = screen_name, user_id = None, max_results = 10000)   
        save_json("ABC",data)