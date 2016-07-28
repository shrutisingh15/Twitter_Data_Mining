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
from extract_tweet_entities import extract_tweet_entities
from harvest_user_timeline import harvest_user_timeline
from get_common_tweet_entities import get_common_tweet_entities
from prettytable import PrettyTable
from analyze_tweet_content import analyze_tweet_content


def analyze_favorites(twitter_api, screen_name, entity_threshold = 2):
    favs = twitter_api.favorites.list(screen_name=screen_name, count = 200)
    print("Number of favorites", len(favs)) 
    common_entities = get_common_tweet_entities(favs, entity_threshold = entity_threshold)
    pt = PrettyTable(field_names=['Entity','Count'])
    [pt.add_row(kv) for kv in common_entities]
    pt.align['Entity'], pt.align['Count'] = 'l','r'
    
    print
    print("Common entities in favourites...")
    print(pt)
    
    print 
    print("Some statitics about the contents of the favorites...")
    analyze_tweet_content(favs)
    
if __name__ == '__main__':
        twitter_api = outh_login()
        screen_name="nytimes"  ## 'nytimes' , 'ABC'
        analyze_favorites(twitter_api, screen_name)
        