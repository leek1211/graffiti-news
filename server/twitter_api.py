import twitter
from config import *

twitter_api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                      consumer_secret=TWITTER_CONSUMER_SECRET,
                      access_token_key=TWITTER_ACCESS_TOKEN,
                      access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

'''
Use google API to query trend words right now.
'''
def get_trend_words():
  woe_america = 23424977
  woe_global = 1
  trends = twitter_api.GetTrendsWoeid(woeid = woe_america)
  

  ret = []
  for trend in trends:
     word = trend.name
     if word[0] == '#':
       word = word[1:]
     ret.append(word)

  return ret






  