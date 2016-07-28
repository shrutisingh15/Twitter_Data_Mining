import twitter
import json
from outh_login import outh_login

## Searching a tweet
def twitter_search(twitter_api,q,max_results=200):
    search_results = twitter_api.search.tweets(q=q,count=100)
    statuses = search_results['statuses']
    
    ## Enforcing a reasonable limit on max_results
    max_results = min(1000,max_results)
    
    for _ in range(10):  #10*100 = 1000 where 100 is the count
        try:
          next_results = search_results['search_metadata']['next_results']
        except KeyError as e:
          break 

    ## create a diction from next_results 
        kwargs = dict([kv.split('=')
                     for kv in next_results[1:].split("&")])
        search_results = twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses'] 

        if len(statuses) > max_results:
          break
          
    return statuses
    
    
if __name__ == '__main__':
      twitter_api = outh_login()
      q = "Hillary Clinton"
      search_results= twitter_search(twitter_api,q,max_results=200)
      print(json.dumps(search_results,indent=1))