import twitter
from config import *

twitter_api = twitter.Api(
  consumer_key=TWITTER_CONSUMER_KEY,
  consumer_secret=TWITTER_CONSUMER_SECRET,
  access_token_key=TWITTER_ACCESS_TOKEN,
  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

def get_woeid(lang):
  if lang == 'ko':
    return 23424868
  if lang == 'en':
    return 23424977
  return 1

'''
Use google API to query trend words right now.
'''
def get_trend_words(lang):
  woeid = get_woeid(lang)
  trends = twitter_api.GetTrendsWoeid(woeid = woeid)

  ret = []
  for trend in trends:
     word = trend.name
     if word[0] == '#':
       word = word[1:]
     ret.append(word)

  return ret






  