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

#Step 3 - Retrieve Tweets
public_tweets = api.search('Olivia')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")