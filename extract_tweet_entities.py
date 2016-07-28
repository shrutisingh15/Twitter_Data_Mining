import twitter

## Extracting tweet entities
def extract_tweet_entities(statuses):
    
    if len(statuses) == 0:
       return [], [], [], []

    screen_names = [user_mention['screen_name']
                      for status in statuses
                          for user_mention in status['entities']['user_mentions']]
    
    hashtags = [hashtag['text']
                  for status in statuses
                      for hashtag in status['entities']['hashtags']]
    
    urls = [url['expanded_url']
                for status in statuses
                    for url in status['entities']['urls']]
                    
    symbols = [symbol['text']
                  for status in statuses
                      for symbol in status['entities']['symbols']]
    '''                  
    for status in statuses:                
       if status['entities']['media']:
          media = [media['url']
                   for status in statuses
                       for media in status['entities']['media']]
       else:
          media =[]
          
     '''
    '''     
    media = [media['url']
                 for status in statuses
                      for media in status['entities']['media']]
    '''
    return screen_names, hashtags, urls, symbols