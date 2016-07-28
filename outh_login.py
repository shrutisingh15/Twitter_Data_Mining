import twitter

## Authentication into Twitter API
def outh_login():
    access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth=twitter.oauth.OAuth(access_token,access_token_secret,consumer_key,consumer_secret)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api