import tweepy 
import math
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "RWhtG4U5XsveVHdJu5EHoxC09" 
consumer_secret = "QSUn5mo7dONRVwRN1H3X7y8ZMZqR84ofuV4YgpPsiVs722lLAV"
access_key = "2998999917-xoknJKUqNn7ytTwf9NNR7Z96PoJDzHYCTpBKyno"
access_secret = "ts4XRe5AzAHbwRtffcAJGR7jX8mhZHN2UxBH9C4k5IvUR"
  
# Function to extract tweets 
def getTweets(username, num): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 

        # Empty Array 
        tmp=[]  
  
        # inputs the text for all the tweets into tmp list
        for i in range(int(math.ceil(num/20))):
            tweets = api.user_timeline(screen_name=username, page = i, tweet_mode="extended") 
            for tweet in tweets:
                tmp.append(tweet.full_text)

        return tmp
        
def getTweetsFast(username, num): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 

        # Empty Array 
        tmp=[]  
  
        tweets = api.user_timeline(screen_name=username, count= num, tweet_mode="extended")
        # inputs the text for all the tweets into tmp list

        for tweet in tweets:
            tmp.append(tweet.full_text)

        return tmp

# print(getTweetsFast("ZackLehman", 20))
