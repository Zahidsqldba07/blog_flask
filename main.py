import asyncio
from db import db
from crypt import methods
from flask import Flask, request, render_template


app = Flask(__name__)
asyncio.run(db.init_app(app))

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
