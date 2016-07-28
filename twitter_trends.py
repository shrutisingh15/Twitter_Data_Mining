import twitter
import json
from outh_login import outh_login

## Discovering the trending topics
def twitter_trends(twitter_api, woe_id):
    trending = twitter_api.trends.place(_id=woe_id)
    return trending
    
if __name__ == '__main__':
      twitter_api = outh_login()
      us_woe_id = 23424977
      world_woe_id = 1
      us_trends = twitter_trends(twitter_api,us_woe_id)
      print(json.dumps(us_trends,indent=1))