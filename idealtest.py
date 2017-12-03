#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:53:31 2017

@author: ericd2017
"""

import http.client
import tweepy
import pandas as pd
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='el1026', api_key='xzMjNZbKYeKWSsQEYdW0')

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#Connect with Emoj API
conn = http.client.HTTPSConnection("www.emoj.ai")

headers = {
    'cache-control': "no-cache",
    'postman-token': "fccfc1bc-2a41-e8f2-2cac-34fadc9639ba"
    }

# Authenticate
consumer_key= 'BAx0g0ef9Ouy4rxNMFFfU3Mp4'
consumer_secret= 'znpm5r0OFpnN9zwR6uHtM08e6KYsImZ6K0oWReqKgeHLsMSBnD'

access_token='809180462790877184-roO2CwSuDMXw7U5e1CJbxBrO8eay9hE'
access_token_secret='87w6y5DAVz0kXSbNJczIoIX9UDSipVRAe933B0aGK170u'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

brand = input('Enter the Brand to find sentiments about: ')

public_tweets = api.search(q=brand, rpp=100, count=1000)
#print(public_tweets)
anxious_values = []

def jsonParser(json):
    json = json.split(':', 2)[-1][2:-2]
    arr = json.split("},{")
    for i in arr:
        if (len(i.split(":")) > 1 and i.split(":")[1].split(",")[0] == '"anxious"'):
            anxious_values.append(int(i.split(":")[2]))        
        #print(i)
        #split by "," handle label, handle value
    return json

def handle_tweets(public_tweets):    
    for tweet in public_tweets:
        try:
            str = tweet.text
            str = ''.join(c for c in str if 0 < ord(c) < 127).replace(" ", "%")
            conn.request("GET", "/api/classify?text=" + str + "&token=RNXkMoBg6RQlV0Nn", 
                         headers=headers)
            res = conn.getresponse()
            analysis = (res.read()).decode("utf-8")
            jsonParser(analysis)
        except  http.client.HTTPException as e:
            return("HTTPException")
        
handle_tweets(public_tweets)

trace0 = go.Scatter(
        x = anxious_values,
        y = list(range(1, len(anxious_values))),
        name = 'Anxiety levels',
        line = dict(
                color = ('rgb(205, 12, 24)'),
                width = 4)
        )

data = [trace0]

layout = dict(title = 'Anxiety levels over subject: ' + brand,
              xaxis = dict(title = 'Frequency'),
              yaxis = dict(title = 'Anxiety'))

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')

#create pandas dataframeD
#a = 0
#data = pd.DataFrame(data=[tweet.text for tweet in public_tweets], columns=['Tweets'])
#data['Date'] = np.array([tweet.created_at for tweet in public_tweets])
#data['emotion'] = np.array([anxious_values])

#temotion = pd.Series(data=data['emotion'].values, index=data['Date'])
#temotion = pd.Series(data=data['emotion'].values, index=data['Date'])
#temotion.plot(figsize=(16,4), color='r')
#temotion.plot(figsize=(16,4), label='Emotion Scale')
