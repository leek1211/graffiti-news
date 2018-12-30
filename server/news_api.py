from newsapi import NewsApiClient
from config import *

news_api = NewsApiClient(api_key=NEWS_API_KEY)

def search_articles(keyword):
  result = news_api.get_everything(q=keyword, sort_by='relevancy', language='en', page_size=30, page=1)
  ret = []
  for a in result['articles']:
    ret.append(
      {
        'url': a['url'],
        'content': a['content'],
        'source': a['source']['name']
      }
    )
  return ret