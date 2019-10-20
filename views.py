import os
from app import app, db
from models import Face, User
from forms import LoginForm
from flask import session, redirect, url_for, render_template, abort, request, flash, Response, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import base64


@app.route('/')
def index():
    return 'okay'


@app.route('/dashboard')
def dashboard():
    user = User.get_by_username(session.get('username', None))
    return render_template("admin.html", balance=user.balance)


@app.route('/camera-in')
def camera_in():
    return render_template('camera_in.html')


@app.route('/camera-out')
def camera_out():
    return render_template('camera_out.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        username, password = form.username.data, form.password.data
        user = User.get_by_username(username)
        if user and user.password == password:
            return redirect(url_for('dashboard'))
        else:
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('signup.html', user_id=new_user.id)
    return render_template('login.html', form=form)


@app.route('/register', methods=['POST'])
def register_by_ui_path():
    data = request.get_json()
    if data:
        image = base64.b64decode(data['photo'])
        name = base64.b64decode(data['name'])
        print(name)
    else:
        print('blah')