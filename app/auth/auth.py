import asyncio
from crypt import methods
import datetime
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from db.db import get_db_collection


bp = Blueprint('auth', __name__, url_prefix='/auth')


class USER_EXIST_EXCEPTION(Exception):
    pass

@bp.route('register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_collection = get_db_collection('user')
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        if error is None:
            try:
                user = {
                    'username': username,
                    'password': password,
                    'timestamp': f'{datetime.timestamp(datetime.now())}'
                }
                user_collection.insert_one(user)

            except USER_EXIST_EXCEPTION:
                error = f'User {username} is already registred'
            else:
                return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register_page.html')

@bp.route('/login', methods=['GET', 'POST'])
async def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_collection = await get_db_collection('user')
        error = None

        user = user_collection.find_one({'username': username})

        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user['_id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login_page.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.before_app_request
def load_loggedin_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db_collection('user').find_one({'_id': user_id})

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view
