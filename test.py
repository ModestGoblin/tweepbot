#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:53:31 2017

@author: ericd2017
"""
#from sets import Set
import http.client
import tweepy
from textblob import TextBlob

#Connect with Emoj API
conn = http.client.HTTPSConnection("www.emoj.ai")

headers = {
    'cache-control': "no-cache",
    'postman-token': "fccfc1bc-2a41-e8f2-2cac-34fadc9639ba"
    }

# Authenticate
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

brand = input('Enter the Brand to find sentiments about: ')

public_tweets = api.search(brand)

def jsonParser(json):
    json = json.split(':', 2)[-1][2:-2]
    arr = json.split("},{")
    for i in arr:
        print(i)
        #split by "," handle label, handle value
    return json

for tweet in public_tweets:
    str = tweet.text
    print(str)
    if str[0] == 'R' and str[1] == 'T':
        str = str.split(':', 1)[-1]
    print(str)
    str.replace(" ", "%")

    conn.request("GET", "/api/classify?text=str&token=RNXkMoBg6RQlV0Nn", headers=headers)
    res = conn.getresponse()
    analysis = (res.read()).decode("utf-8")

    #jsonParser(analysis)

    #print(analysis)
    #print("\n")


    '''
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
conn.request("GET", "/api/classify?text=I%20am%20sad&token=RNXkMoBg6RQlV0Nn", headers=headers)

res = conn.getresponse()
data = res.read()

str = "I am happy"
str.replace(" ", "%")
print(str)

conn.request("GET", "/api/classify?text=str&token=RNXkMoBg6RQlV0Nn", headers=headers)

res2 = conn.getresponse()
data2 = res2.read()

print(data.decode("utf-8"))
print("/n")
print(data2.decode("utf-8"))
'''
