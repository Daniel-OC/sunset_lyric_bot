import requests
import tweepy


tweet = requests.get(url = "https://selling-sunset-lyrics-api.herokuapp.com/api/v1/lyrics/random").json()

print(tweet)