import os
import sys
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app
import MySQLdb
from webapp import db
# db, bcrypt, mail
# from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                              PostForm, RequestResetForm, ResetPasswordForm)
# from flaskblog.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message

def connect_to_cloudsql():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        cloudsql_unix_socket = os.path.join(
            '/cloudsql', 'kancolledb-project:australia-southeast1:kancolle-mysql')

        db_connection = MySQLdb.connect(
                            unix_socket=cloudsql_unix_socket,
                            user='root',
                            passwd='kancolledbpw',
                            db='admin'
                            )
    else:
        db_connection = MySQLdb.connect(
                       host='127.0.0.1', user='root', passwd='kancolledbpw', db='admin')
    return db_connection

# Connect to our database
try: 
    con = MySQLdb.connect("127.0.0.1", "root", "kancolledbpw", "admin")
    # con = connect_to_cloudsql()
    cur = con.cursor()
except Exception as e:
    sys.exit(e)

@app.route('/')
@app.route("/home")
def homepage():
    return render_template('homepage.html')

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

@app.route('/loginpage')
def login():
    return render_template('loginpage.html')

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
