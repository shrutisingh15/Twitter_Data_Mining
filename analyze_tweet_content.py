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
import pandas
from bokeh.charts import Bar, Scatter, output_file, show
from flask import Flask,render_template
from bokeh.embed import file_html,components

def analyze_tweet_content(statuses):
    if len(statuses) == 0:
       print("No content to analyze")
       return
    ## A nested helper function to calculate lexical diversity
    def lexical_diversity(tokens):
        return 1.0*len(set(tokens))/len(tokens)
        
    ## A nested helper function to calculate the average number of words per tweet
    def average_words(statuses):
        total_words = sum([len(s.split()) for s in statuses])
        return 1.0*total_words/len(statuses)
    
    status_texts=[status['text'] for status in statuses]
    screen_names, hashtags, urls, _ = extract_tweet_entities(statuses)
    
    words = [w 
            for text in status_texts
                for w in text.split()]
                
    print("Lexical Diversity of words", lexical_diversity(words))
    print("Lexical Diversity of user mentions screen names", lexical_diversity(screen_names))
    print("Lexical Diversity of urls", lexical_diversity(urls))
    print("Lexical Diversity of hashtags", lexical_diversity(hashtags))
    
    ld_words = lexical_diversity(words)
    ld_urls = lexical_diversity(urls)
    ld_hashtags = lexical_diversity(hashtags)
    
    return ld_words, ld_urls, ld_hashtags
    
    
def prepare_data(twitter_api):
    name = "nytimes" 
    data = harvest_user_timeline(twitter_api, screen_name = name, user_id = None, max_results = 1000)
    ld_words, ld_urls, ld_hashtags = analyze_tweet_content(data)     
    c1 = pandas.Series([name,name,name], name = "Newspaper")
    c2 = pandas.Series([ld_words,ld_urls,ld_hashtags], name = "Lexical Diversity")
    c3 = pandas.Series(['words','urls','hashtags'], name = "Type")
    nytimes_data = pandas.concat([c1,c2,c3],axis=1)
    
    name = "washingtonpost" 
    data = harvest_user_timeline(twitter_api, screen_name = name, user_id = None, max_results = 1000)
    ld_words, ld_urls, ld_hashtags = analyze_tweet_content(data) 
    c1 = pandas.Series([name,name,name], name = "Newspaper")
    c2 = pandas.Series([ld_words,ld_urls,ld_hashtags], name = "Lexical Diversity")
    c3 = pandas.Series(['words','urls','hashtags'], name = "Type")
    washingtonpost_data = pandas.concat([c1,c2,c3],axis=1)
    
    name ="WSJ"
    data = harvest_user_timeline(twitter_api, screen_name = name, user_id = None, max_results = 1000)
    ld_words, ld_urls, ld_hashtags = analyze_tweet_content(data)             
    c1 = pandas.Series([name,name,name], name = "Newspaper")
    c2 = pandas.Series([ld_words,ld_urls,ld_hashtags], name = "Lexical Diversity")
    c3 = pandas.Series(['words','urls','hashtags'], name = "Type")
    WSJ_data = pandas.concat([c1,c2,c3],axis=1)    
    
    name = "USATODAY"
    data = harvest_user_timeline(twitter_api, screen_name = name, user_id = None, max_results = 1000)
    ld_words, ld_urls, ld_hashtags = analyze_tweet_content(data)           
    c1 = pandas.Series([name,name,name], name = "Newspaper")
    c2 = pandas.Series([ld_words,ld_urls,ld_hashtags], name = "Lexical Diversity")
    c3 = pandas.Series(['words','urls','hashtags'], name = "Type")
    USATODAY_data = pandas.concat([c1,c2,c3],axis=1)
    
    name = "guardian"
    data = harvest_user_timeline(twitter_api, screen_name = name, user_id = None, max_results = 1000)
    ld_words, ld_urls, ld_hashtags = analyze_tweet_content(data)         
    c1 = pandas.Series([name,name,name], name = "Newspaper")
    c2 = pandas.Series([ld_words,ld_urls,ld_hashtags], name = "Lexical Diversity")
    c3 = pandas.Series(['words','urls','hashtags'], name = "Type")
    guardian_data = pandas.concat([c1,c2,c3],axis=1) 
    
    final_data = pandas.concat([nytimes_data,washingtonpost_data,WSJ_data,USATODAY_data,guardian_data], axis=0)
    return final_data
    
if __name__ == '__main__':
        twitter_api = outh_login()
        datacsv = prepare_data(twitter_api)
        datacsv.to_csv("datacsv.csv")



    



           
            
           
        
         
        
 
        
 
        
        
        
       
        
        
        
      
        
        