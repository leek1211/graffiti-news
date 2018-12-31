from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

from twitter_api import get_trend_words
from news_api import search_articles
from giphy_api import get_giphy as get_gifs

app = Flask(__name__)
CORS(app)

@app.route('/graffiti')
def get_graffiti():
  try:
    lang = request.args.get('lang')
    if lang == None:
      lang = 'en'

    trend_words = get_trend_words(lang)[:3]
    return jsonify(trends=get_gifs(trend_words, lang)), 200
  except:
    return jsonify(message = 'internal server error'), 500

@app.route('/articles')
def get_articles():
  try:
    keyword = request.args.get('keyword')
    if keyword == None:
      msg = "Wrong keyword input %s" % keyword
      return jsonify(message=msg), 400

    lang = request.args.get('lang')
    if lang == None:
      lang = 'en'

    giphy_response = get_gifs([keyword], lang)
    if len(giphy_response) == 0:
      return jsonify(message = 'no matching images found'), 400
    images = giphy_response[0]['images']
    articles = search_articles(keyword, lang)
    return jsonify(images = images, articles=articles), 200
  except:
    return jsonify(message = 'internal server error'), 500

