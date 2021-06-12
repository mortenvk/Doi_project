from flask import Flask
from getaway import app, conn, bcrypt
from getaway.forms import RegForm, LoginForm
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from getaway.models import Customers, select_Customers, insert_Customers
from psycopg2 import sql

Login = Blueprint('Login', __name__)

posts = [{}]


@Login.route("/")
@Login.route("/home")
def home():
    return render_template('home.html', posts = posts)


@Login.route("/register", methods=['GET', 'POST'])
def register(): 
    form = RegForm()
    if form.validate_on_submit():
        email = form.email.data
        likes_heat = form.likes_heat.data
        plane_pref = form.plane_pref.data
        boat_pref = form.boat_pref.data
        train_pref = form.train_pref.data

        budget = form.budget.data
        password = form.password.data
        name = form.username.data
        insert_Customers(email, likes_heat, plane_pref, boat_pref, train_pref, budget, password, name) 
        flash('Your account has been created!')
        return redirect(url_for('Login.home'))
    return render_template('reg.html', form=form)
    

@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Login.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = select_Customers(form.email.data)
        password = form.password.data
        if user != None and user[6] == form.password.data:
            login_user(user, remember=form.remember.data)
            flash('Login successful.','success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Login.home'))
        else:
            flash('Login Unsuccessful. Please check identifier and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.home'))


'''@Login.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')'''
