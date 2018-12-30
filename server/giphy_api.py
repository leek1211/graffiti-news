import json
import requests
from config import *

def extract_keyword_and_urls(keyword, body):
  data = body['data']
  images = []
  for obj in data:
    images.append(
      {
        'url': obj['images']['original']['url'],
        'height': obj['images']['original']['height'],
        'width': obj['images']['original']['width']
      }
    )
  return {
    'keyword': keyword,
    'images': images
  }

'''
Use GIPHY API to find the gif urls of the given words
'''
def get_giphy(keywords):
  url = 'http://api.giphy.com/v1/gifs/search'
  payload = {
    'api_key': GIPHY_API_KEY,
    'offset': 0,
    'limit': 10
  }
  ret = []
  for keyword in keywords:
    payload['q'] = keyword
    response = requests.get(url, params = payload)
    response_body = response.json()
    elem = extract_keyword_and_urls(keyword, response_body)
    if len(elem['images']) >= 5:
      ret.append(elem)

    if len(ret) == 10:
      break

  return ret

