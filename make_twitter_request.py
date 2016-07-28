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


## Making robust requests in twitter
def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
        if wait_period > 3600:
           print('Too many retries. Quitting.', file = sys.stderr)
           raise e
           
        if e.e.code == 401:
           print('Encountered 401 Error (Not Authorized)', file=sys.stderr)
           return None
        elif e.e.code == 404:
           print('Encountered 404 Error (Not Found)', file = sys.stderr)
           return None
        elif e.e.code == 429:
           print('Encountered 429 Error (Rate Limit Exceeded)', file = sys.stderr)
           if sleep_when_rate_limited:
              print("Retrying in 15 minutes...ZzZ...", file = sys.stderr)
              sys.stderr.flush()
              time.sleep(60*15 + 5)
              print('...ZzZ...Awake now and trying again.', file = sys.stderr)
              return 2
           else:
               raise e
        elif e.e.code in (500, 502, 503, 504):
            print('Encountered %i Error. Retrying in %i seconds' % \
             (e.e.code, wait_period), file=sys.stderr)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e
            
    wait_period = 2
    error_count = 0
    while True:
        try:
           return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError as e:
           error_count = 0
           wait_period = handle_twitter_http_error(e, wait_period)
           if wait_period is None:
              return
        except URLError as e:
           error_count += 1
           print("URLError encountered. Continuing.", file = sys.stderr)
           if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file = sys.stderr)
                raise
        except BadStatusLine as e:
           error_count += 1
           print("BadStatusLine encountered. Continuing.", file = sys.stderr)
           if error_count > max_errors:
                print("Too many consecutive errors...bailing out.", file = sys.stderr)
                raise
