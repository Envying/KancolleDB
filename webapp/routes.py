import os
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app
# db, bcrypt, mail
# from webapp.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                              PostForm, RequestResetForm, ResetPasswordForm)
# from webapp.models import User, Post
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, logout_user, UserMixin
# from flask_mail import Message
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
@app.route("/home")
def homepage():
    return render_template('homepage.html')

@app.route('/world_maps')
def world_maps():
    return render_template('world_maps.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/loginpage')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline')
    session['oauth_state'] = state
    return render_template('loginpage.html', auth_url=auth_url)

@app.route('/oAuthcallback')
def callback():
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('index'))
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
            return redirect(url_for('index'))
        return 'Could not fetch your information.'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
