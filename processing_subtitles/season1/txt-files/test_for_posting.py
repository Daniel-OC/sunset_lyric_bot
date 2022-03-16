import requests
import json

url = 'https://selling-sunset-lyrics-api.herokuapp.com/api/v1/lyrics'

headers = {'Content-Type': 'text/text; charset=utf-8'}
text = "♪ You'll be okay♪♪ A beautiful day♪"
r = requests.post(url,data = json(text.encode('utf-8')), headers = headers)
print(r.text)

# lyrics_formatted[1]


# for i in range(0, len(lyrics_formatted)-1):
#   requests.post(url, data= lyrics_formatted[i].encode('utf-8'), headers = headers)