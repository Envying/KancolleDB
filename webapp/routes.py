import os
import sys
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app
import MySQLdb
from webapp import db, models
from models import FleetComposition
# db, bcrypt, mail
# from flaskblog.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                              PostForm, RequestResetForm, ResetPasswordForm)
# from flaskblog.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message

# Connect to our database
try: 
    con = MySQLdb.connect("127.0.0.1", "root", "kancolledbpw", "admin")
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
    ship_data = cur.fetchall()

    ship_name = []
    ship_class = []

    for row in ship_data:
        ship_name.append(row[1])
        ship_class.append(row[2])

    # Get composition data
    cur.execute("SELECT * FROM fleet_composition WHERE world_map = \"world_1_1\"")
    fleet_composition_1_1 = cur.fetchall()

    return render_template('world_maps.html', ship_name=ship_name, ship_class=ship_class, 
        fleet_composition_1_1=fleet_composition_1_1)

@app.route('/loginpage')
def login():
    return render_template('loginpage.html')

@app.route('/post_comp', methods=['POST'])
def post_comp():
    # from flask import jsonify
    name = request.form['ship_name0']
    ship_class = request.form['ship_class0']
    name2 = request.form['ship_name1']
    ship_class2 = request.form['ship_class1']
    name3 = request.form['ship_name2']
    ship_class3 = request.form['ship_class2']
    name4 = request.form['ship_name3']
    ship_class4 = request.form['ship_class3']
    name5 = request.form['ship_name4']
    ship_class5 = request.form['ship_class4']
    name6 = request.form['ship_name5']
    ship_class6 = request.form['ship_class5']
    world_map = request.form['set-map']

    insert_statement = (
                "INSERT INTO fleet_composition (name, ship_class, name2, ship_class2, "
                "name3, ship_class3, name4, ship_class4, name5, ship_class5, "
                "name6, ship_class6, world_map) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )
    values = (name, ship_class, name2, ship_class2, name3, ship_class3, name4, ship_class4, 
        name5, ship_class5, name6, ship_class6, world_map)

    cur.execute(insert_statement, values)
    con.commit()

    # return jsonify(test)
    return render_template('homepage.html')
