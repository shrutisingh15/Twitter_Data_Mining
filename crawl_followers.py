import twitter
import json
from get_friends_followers_ids import get_friends_followers_ids
from outh_login import outh_login
from save_json import save_json


## Data collection to crawl a friendsship graph
def crawl_followers(twitter_api,screen_name,limit=100,depth = 2):
    seed_id = str(twitter_api.users.show(screen_name=screen_name)['id'])
    _, next_queue = get_friends_followers_ids(twitter_api,user_id=seed_id,friends_limit=0,followers_limit=limit)
    data=({'followers':[_id for _id in next_queue]}, 'followers_crawl','{0}-follower_ids'.format(seed_id))
    save_json('crawl',data)
    d=1
    while d<depth:
          d += 1
          (queue,next_queue) = (next_queue,[])
          for fid in queue:
              followers_ids = get_friends_followers_ids(twitter_api,user_id=fid,friends_limit=0,followers_limit=limit)
              
              data1 = ({'followers' : [ _id for _id in next_queue ]},'followers_crawl', '{0}-follower_ids'.format(fid))
              save_json('crawling-{0}'.format(screen_name),data1)
              next_queue += followers_ids
              
              
if __name__ == '__main__':
    twitter_api = outh_login()
    screen_name ="LordSnow"
    crawl_followers(twitter_api,screen_name,depth=2,limit=10)