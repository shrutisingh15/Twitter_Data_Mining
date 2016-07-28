import twitter
import json
from outh_login import outh_login
from make_twitter_request import make_twitter_request


## resolving user profile information
def get_user_profile(twitter_api,screen_names=None,user_ids=None):
    assert (screen_names != None) != (user_ids !=None)
    items_to_info = {}
    items = screen_names or user_ids
    while len(items) > 0:
         items_str = ','.join([str(item) for item in items[:100]])
         items = items[100:]
         
         if screen_names:
            response = make_twitter_request(twitter_api.users.lookup,screen_name=items_str)
         else:
            response = make_twitter_request(twitter_api.users.lookup,user_ids=items_str)   

    for user_info in response:
        if screen_names:
            items_to_info[user_info['screen_name']]=user_info       
        else:
            items_to_info[user_info['id']]= user_info        
            
    return items_to_info
    
    
if __name__ == '__main__':
        twitter_api = outh_login()
        screen_name ="LordSnow"  ## Getting the user profile of jon Snow character of Game of thrones
        info = get_user_profile(twitter_api,screen_names=screen_name)
        print(json.dumps(info,indent=1))