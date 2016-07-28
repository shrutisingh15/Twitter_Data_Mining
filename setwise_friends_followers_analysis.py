import twitter
import json
from functools import partial
from sys import maxsize
from outh_login import outh_login
from make_twitter_request import make_twitter_request
from get_friends_followers_ids import get_friends_followers_ids

def setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids):
    friends_ids, followers_ids = set(friends_ids), set(followers_ids)
    
    print('{0} is following {1}'.format(screen_name, len(friends_ids)))
    print('{0} is being followed by {1}'.format(screen_name, len(followers_ids)))
    print('{0} of {1} are not following {2} back'.format(len(friends_ids.difference(followers_ids)),len(friends_ids), screen_name))
    print('{0} of {1} are not being followed back by {2}'.format(len(followers_ids.difference(friends_ids)),len(followers_ids), screen_name))
    print('{0} has {1} mutual friends'.format(screen_name, len(friends_ids.intersection(followers_ids))))
    
    
    
if __name__ == '__main__':
      twitter_api = outh_login()
      screen_name ="HillaryClinton"
      friends_ids, followers_ids = get_friends_followers_ids(twitter_api,screen_name=screen_name,friends_limit=5000,followers_limit=5000)
      setwise_friends_followers_analysis(screen_name, friends_ids, followers_ids)