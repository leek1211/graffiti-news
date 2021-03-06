import json
import requests
from config import *

def get_channel_names(keyword):
  channel_search_api_url = 'https://giphy.com/api/v1/channels-search/search/channel_v2'
  # print('Sending request ', keyword)
  channel_search_result = requests.get(channel_search_api_url, params = {'q': keyword}).json()
  channel_names = []
  for h in channel_search_result['hits']:
    channel_names.append(h['name'])
  
  if len(channel_names) <= 2:
    channel_names.append("")
  else:
    channel_names = [""]

  return channel_names

def get_keyword_giphy(keyword, lang):
  max_image_size = 10
  url = 'http://api.giphy.com/v1/gifs/search'
  payload = {
    'offset': 0,
    'limit': 10,
    'lang': lang,
  }
  channel_names = get_channel_names(keyword)
  
  images = []
  for i, chn in enumerate(channel_names):
    sz = max_image_size / len(channel_names)
    if i == len(channel_names) - 1:
      sz += max_image_size % len(channel_names)
    sz = int(sz)
    
    payload['q'] = keyword + ' ' + chn
    # print('Sending request ', keyword)
    global flag_idx
    payload['api_key'] = GIPHY_API_KEY[flag_idx]
    flag_idx = flag_idx ^ 1
    response_body = requests.get(url, params = payload).json()
    
    if response_body['data'] == None:
      print(keyword, response_body)
    data = response_body['data'][:sz]
    
    for obj in data:
      images.append(
        {
          'url': obj['images']['original']['url'],
          'height': obj['images']['original']['height'],
          'width': obj['images']['original']['width']
        }
      )
  
  return {'images': images, 'keyword': keyword}

def get_giphy_image_from_translate(keyword, lang):
  payload = {
    'lang': lang,
  }
  payload['s'] = keyword
  url = 'http://api.giphy.com/v1/gifs/translate'
  # print('Sending request ', keyword)
  global flag_idx
  payload['api_key'] = GIPHY_API_KEY[flag_idx]
  flag_idx = flag_idx ^ 1
  response_body = requests.get(url, params = payload).json()
  obj = response_body['data']
  return {
    'url': obj['images']['original']['url'],
    'height': obj['images']['original']['height'],
    'width': obj['images']['original']['width']
  }

'''
Use GIPHY API to find the gif urls of the given words
'''
def get_giphy(keywords, lang):
  ret = []
  
  for keyword in keywords:
    elem = get_keyword_giphy(keyword, lang)
    translated = []
    
    try:
      translated.append(get_giphy_image_from_translate(keyword, lang))
    except:
      print ('api limit exceed in translate api')

    elem['images'] = translated + elem['images']
    
    if len(elem['images']) >= 5:
      ret.append(elem)

    if len(ret) == 10:
      break

  return ret
