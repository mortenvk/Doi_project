from flask import render_template, url_for, flash, redirect, request, Blueprint
from getaway import app, conn, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

Login = Blueprint('Login', __name__)

posts = [{}]

@app.route('/')
def index():
    return 'index'

@Login.route("/test")
def index_test():
    return render_template('layout.html', title='name')

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))



