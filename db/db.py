import os
import time
import logging
import click
from pymongo import MongoClient

from flask import current_app, g
from flask.cli import with_appcontext


MONGODB_ENV = 'MONGODB_NAME'
os.environ[MONGODB_ENV] = 'blog'
MONGODB_NAME = os.getenv(MONGODB_ENV)

logger = logging.getLogger('foo.log')
logger.setLevel(logging.DEBUG)


class MongoDBCollectionException(Exception):
    pass

def get_db():
    if 'client' not in g:
        g.client = MongoClient('mongodb://localhost:27017')
        g.client.db = MONGODB_NAME

    return g.client.db

def close_db(exception=None):
    db = g.pop('client', None)
    if db is not None:
        db.close()

async def get_db_collection(collection, backoff_factor=.1):
    db = get_db()
    try:
        return db[collection]
    except MongoDBCollectionException:
        time.sleep(backoff_factor)
        return await get_db_collection(collection, backoff_factor * 2)

@click.command('init-db')
@with_appcontext
def init_db_command():
    get_db()
    click.echo('Initialized MongoDB')

async def init_app(app):
    with app.app_context():
        app.teardown_appcontext(close_db)
        app.cli.add_command(init_db_command)
