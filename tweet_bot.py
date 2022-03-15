import requests
import tweepy
from os import environ
import time

# import the environment details from
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_key = environ['access_key']
access_key_secret = environ['access_key_secret']

# sign into twittter and set up the ability to tweet
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_key_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

interval = 60

while True:
  print("about to tweet a lyric")
# fetch a tweet from the api
  tweet = requests.get(url = "https://selling-sunset-lyrics-api.herokuapp.com/api/v1/lyrics/random").json()
  
  # tweet
  api.update_status(tweet)
  time.sleep(interval)


