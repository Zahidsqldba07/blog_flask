from crypt import methods
import os
import time
import logging
from pymongo import MongoClient
from flask import Flask, request, render_template

MONGODB_ENV = 'MONGODB_NAME'
os.environ[MONGODB_ENV] = 'blog'
MONGODB_NAME = os.getenv(MONGODB_ENV)

logger = logging.getLogger('foo.log')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)


class MongoDBCollectionException(Exception):
    pass

async def get_db_collection(collection, backoff_factor=.1):
    client = MongoClient('mongodb://localhost:27017')
    db = client[MONGODB_NAME]

    try:
        return db[collection]
    except MongoDBCollectionException:
        time.sleep(backoff_factor)
        return get_db_collection(collection, backoff_factor * 2)

portfolio = get_db_collection('portfolio')

@app.route('/')
def home_page(props=None):
    return render_template('home_page.html', props=props)

@app.route('/portfolio', methods=('GET'))
def fetch_portfolios(props=None):
    return render_template('portfolio_page.html', props=props)

@app.route('/portfolio/editor', methods=('POST'))
def create_portfolio(props=None):
    return render_template('portfolio_editor_page.html', props=props)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found_page.html'), 404
