# -*- coding: utf-8 -*-
import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'BAx0g0ef9Ouy4rxNMFFfU3Mp4'
consumer_secret= 'znpm5r0OFpnN9zwR6uHtM08e6KYsImZ6K0oWReqKgeHLsMSBnD'

access_token='809180462790877184-roO2CwSuDMXw7U5e1CJbxBrO8eay9hE'
access_token_secret='87w6y5DAVz0kXSbNJczIoIX9UDSipVRAe933B0aGK170u'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

brand = raw_input('Enter the Brand to find sentiments about: ')
public_tweets = api.search(brand) # 1
positive_tweets = 0.0 # 2 
total_tweets = 0.0




for tweet in public_tweets:

	
	#Step 4 Perform Sentiment Analysis on Tweets
	analysis = TextBlob(tweet.text)
	print(tweet.text)
	total_tweets += 1.0

	if analysis.sentiment.polarity > 0:
		Label = 'POSITIVE'
		positive_tweets += 1.0
	else:
		Label = 'NEGATIVE'


if positive_tweets/total_tweets > 0.8:
	print("😍" + brand)

elif positive_tweets/total_tweets > 0.5:
	print('🙂 ' + brand)

elif positive_tweets/total_tweets > 0.3:
	print('🤔 ' + brand)
else:
	print('😡 ' + brand)

#print(analysis)
print(total_tweets)
print(positive_tweets)
print(tweet.text)

