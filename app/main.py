from flask import Flask, render_template

from db import db
from auth import auth

app = Flask(__name__)
app.config['ENV'] = 'development'
db.init_app(app)
app.register_blueprint(auth.bp)


@app.route('/')
def home_page(props=None):
    return render_template('home_page.html', props=props)

@app.route('/portfolio', methods=['GET'])
def fetch_portfolios(props=None):
    return render_template('portfolio_page.html', props=props)

@app.route('/portfolio/editor', methods=['GET', 'POST'])
def create_portfolio(props=None):
    return render_template('portfolio_editor_page.html', props=props)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found_page.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
