import os
import json
import httplib2
import sys
import MySQLdb
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, session
from webapp import app, db
from webapp.oauth import get_google_auth, Auth
from webapp.models import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, logout_user, UserMixin
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
from flask_sqlalchemy import SQLAlchemy
from webapp.cloudsql import connect_to_cloudsql

# Connect to our database
try:
    # con = MySQLdb.connect("127.0.0.1", "root", "kancolledbpw", "admin")
    con = connect_to_cloudsql()
    cur = con.cursor()
except Exception as e:
    sys.exit(e)

@app.route('/')
@app.route("/home")
def homepage():
    return render_template('homepage.html')

# Routes to world maps page
@app.route('/world_maps')
def world_maps():
    # Get ship data
    cur.execute("SELECT * FROM ship")

    ship_name = []
    ship_class = []
    usage_1_1 = []

    for row in cur.fetchall():
        ship_name.append(row[1])

        if row[2] not in ship_class:
            ship_class.append(row[2])

    # Get composition data
    cur.execute("SELECT * FROM fleet_composition WHERE world_map = \"world_1_1\"")
    fleet_composition_1_1 = cur.fetchall()

    # Get top 10 used ships from world 1-1
    cur.execute("SELECT name, ship_class FROM ship WHERE world_1_1 >= 1 ORDER BY world_1_1 DESC LIMIT 10")
    usage_1_1 = cur.fetchall()

    return render_template('world_maps.html', ship_name=ship_name, ship_class=ship_class,
        fleet_composition_1_1=fleet_composition_1_1, usage_1_1=usage_1_1)

# Routes to login page, uses Flask-Login to check if user is authenticated
@app.route('/loginpage')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline', include_granted_scopes='true')
    session['oauth_state'] = state
    return render_template('loginpage.html', auth_url=auth_url)

# Logs user out when logout is clicked, user must be logged in
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

# Checks if user is authenticated, once logged in it stores the information into the database
@app.route('/oAuthcallback')
def callback():
    if current_user.is_authenticated:
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

@app.route('/post_comp', methods=['POST'])
def post_comp():
    # Get form data for compositions
    composition = []
    composition.append(request.form['ship_name0'])
    composition.append(request.form['ship_class0'])
    composition.append(request.form['ship_name1'])
    composition.append(request.form['ship_class1'])
    composition.append(request.form['ship_name2'])
    composition.append(request.form['ship_class2'])
    composition.append(request.form['ship_name3'])
    composition.append(request.form['ship_class3'])
    composition.append(request.form['ship_name4'])
    composition.append(request.form['ship_class4'])
    composition.append(request.form['ship_name5'])
    composition.append(request.form['ship_class5'])
    composition.append(request.form['set-map'])

    insert_statement = (
                "INSERT INTO fleet_composition (name, ship_class, name2, ship_class2, "
                "name3, ship_class3, name4, ship_class4, name5, ship_class5, "
                "name6, ship_class6, world_map) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )

    # Insert fleet composition to table
    cur.execute(insert_statement, composition)

    # Update stats table
    for i in range(0, 12, 2):
        update_statement = (
            "UPDATE ship SET %s = %s + 1 WHERE name = \'%s\' " % (composition[-1], composition[-1], composition[i])
        )
        cur.execute(update_statement)
    con.commit()

    return render_template('homepage.html')
