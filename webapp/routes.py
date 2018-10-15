import os
import json
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, session
from webapp import app, db
from webapp.oauth import get_google_auth
from webapp.config import Auth
from webapp.models import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, logout_user, UserMixin
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
from flask_sqlalchemy import SQLAlchemy

# Default homepage route
@app.route('/')
@app.route("/home")
def homepage():
    return render_template('homepage.html')

# Routes to world maps page
@app.route('/world_maps')
def world_maps():
    return render_template('world_maps.html')

# Routes to login page, uses Flask-Login to check if user is authenticated
@app.route('/loginpage')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline')
    session['oauth_state'] = state
    return render_template('loginpage.html', auth_url=auth_url)

# Checks if user is authenticated, once logged in it stores the information into the database
@app.route('/oAuthcallback')
def callback():
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('homepage'))
    if 'error' in request.args:
        if request.args.get('error') == 'access_denied':
            return 'You denied access.'
        return 'Error encountered.'
    if 'code' not in request.args and 'state' not in request.args:
        return redirect(url_for('login'))
    else:
        google = get_google_auth(state=session['oauth_state'])
        try:
            token = google.fetch_token(
                Auth.TOKEN_URI,
                client_secret=Auth.CLIENT_SECRET,
                authorization_response=request.url)
        except HTTPError:
            return 'HTTPError occurred.'
        google = get_google_auth(token=token)
        resp = google.get(Auth.USER_INFO)
        if resp.status_code == 200:
            user_data = resp.json()
            email = user_data['email']
            user = User.query.filter_by(email=email).first()
            if user is None:
                user = User()
                user.email = email
            user.name = user_data['name']
            print(token)
            user.tokens = json.dumps(token)
            user.avatar = user_data['picture']
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('homepage'))
        return 'Could not fetch your information.'

# Logs user out when logout is clicked, user must be logged in
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
