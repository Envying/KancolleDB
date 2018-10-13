import os
# import secrets
# from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from webapp import app
# db, bcrypt, mail
# from webapp.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
#                              PostForm, RequestResetForm, ResetPasswordForm)
# from webapp.models import User, Post
# from flask_login import login_user, current_user, logout_user, login_required
# from flask_mail import Message

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
    return render_template('loginpage.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
