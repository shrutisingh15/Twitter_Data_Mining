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

## Getting all friends and followers of a user         
def get_friends_followers_ids(twitter_api,screen_name=None,user_id=None,friends_limit=maxsize,followers_limit=maxsize):
    assert (screen_name != None) != (user_id != None) 
    friends_ids, followers_ids = [], []
    
    get_friends_ids = partial(make_twitter_request,twitter_api.friends.ids,count=5000)    
    get_followers_ids = partial(make_twitter_request, twitter_api.followers.ids,count=5000)
    
    
    for twitter_api_func, limit, ids, label in [
                   [get_friends_ids, friends_limit, friends_ids, "friends"],
                   [get_followers_ids, followers_limit, followers_ids, "followers"]
                  ]:

         
        if limit == 0: continue
        cursor = -1
        while cursor !=0:
              if screen_name:
                 response = twitter_api_func(screen_name=screen_name,cursor=cursor)
              else:
                 response = twitter_api_func(user_id=user_id, cursor=cursor)
                 
              if response is not None:
                 ids +=response['ids']
                 cursor=response['next_cursor']
              print('Fetched {0} total {1} ids for {2}'.format(len(ids),label,(user_id or screen_name)), file = sys.stderr)
              
              if len(ids) >=limit or response is None:
                 break
    return friends_ids[:friends_limit], followers_ids[:followers_limit]
    
    
if __name__ == '__main__':
   twitter_api = outh_login()
   screen_name ="HillaryClinton"
   friends_ids, followers_ids = get_friends_followers_ids(twitter_api,screen_name=screen_name,friends_limit=20,followers_limit=20)
   print("Printing Friend ids...")
   print(friends_ids)
   print("Printing Follower ids...")
   print(followers_ids)
   