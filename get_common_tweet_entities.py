import twitter
from extract_tweet_entities import extract_tweet_entities
from collections import Counter

## finding the most popular tweet entities in a collection of tweets        
def get_common_tweet_entities(statuses,entity_threshold=3):
    tweet_entities = [ e
                       for status in statuses
                           for entity_type in extract_tweet_entities([status])
                                for e in entity_type
    ]
    c= Counter(tweet_entities).most_common()
    return [ (k,v)
              for (k,v) in c
                  if v>= entity_threshold
    ]
    