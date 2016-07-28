import twitter
import json
from outh_login import outh_login
from make_twitter_request import make_twitter_request
from harvest_user_timeline import harvest_user_timeline
from save_json import save_json
from bokeh.charts import Histogram, output_file, show
import pandas

## Finding the most popular tweets in a collection of tweets
def find_popular_tweets(twitter_api,statuses,retweet_threshold=3):
    return [ status 
                for status in statuses
                    if status['retweet_count'] > retweet_threshold
    ]

    
if __name__ == '__main__':
        twitter_api = outh_login()
        screen_name = "nytimes"
        data = harvest_user_timeline(twitter_api, screen_name = screen_name, user_id = None, max_results = 10000)
        ##save_json('nytimes-tweetdata',data)        
        popular_tweets = find_popular_tweets(twitter_api,data)
        ##save_json('nytimes-populartweetdata',popular_tweets)
        retweet_count=[]
        favourite_count=[]
        for tweet in popular_tweets:
            if(tweet['retweet_count']) > 50:
               retweet_count.append(tweet['retweet_count'])
               favourite_count.append(tweet['favorite_count'])
            print("Retweeted Count:",tweet['retweet_count'])
            print("Text of the tweet...")
            print(tweet['text'])
            print("-------------------------------------------------------------------------------------------------------------------")
        dataset = pandas.DataFrame()
        dataset['Retweet_Count'] = retweet_count
        dataset['Favorite_Count'] = favourite_count

        dataset.to_csv("dataset1.csv")     ## saving the data to a csv file for later use   
        
        