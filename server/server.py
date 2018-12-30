from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

from giphy_api import get_giphy
from twitter_api import get_trend_words
from news_api import search_articles

app = Flask(__name__)
CORS(app)

@app.route('/graffiti')
def get_graffiti():
  trend_words = get_trend_words()
  return jsonify(trends=get_giphy(trend_words)), 200

@app.route('/articles')
def get_articles():
  keyword = request.args.get('keyword')
  if keyword == None:
    msg = "Wrong keyword input %s" % keyword
    return jsonify(message=msg), 400
  
  giphy_response = get_giphy([keyword])
  if len(giphy_response) == 0:
    return jsonify(message = 'no matching images found'), 400
  images = giphy_response[0]['images']
  articles = search_articles(keyword)
  return jsonify(images = images, articles=articles), 200

