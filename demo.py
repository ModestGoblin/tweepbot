# -*- coding: utf-8 -*-
from config import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
from textblob import TextBlob

"""
# insert Twitter API keys below
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''
"""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

brand = raw_input('Enter the Brand to find sentiments about: ')
public_tweets = api.search(brand) # 1
positive_tweets = 0.0 # 2
total_tweets = 0.0




for tweet in public_tweets:


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
	print(Label)
	print("\n")
print(total_tweets)
print(positive_tweets)
print(tweet.text)
