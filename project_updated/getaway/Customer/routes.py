from flask import render_template, url_for, flash, redirect, request, Blueprint
from getaway import app, conn, bcrypt
from flask_login import current_user
from getaway.models import Customers, select_Customers, insert_Customers, Countries, hot_countries, cont_all
import sys, datetime

Customer = Blueprint('Customer', __name__)

@Customer.route("/destination", methods=['GET', 'POST'])
def continents():
    if not current_user.is_authenticated:
        flash('Please Login.','danger')
        return redirect(url_for('Login.login'))
    
    print(current_user)
    prefs = [current_user.plane_pref, current_user.boat_pref, current_user.train_pref]
    destination = hot_countries(current_user.likes_heat, current_user.budget)
    
    print(destination)
    return render_template('destination.html', destinations = destination, title='Destination', preferences = prefs)

@Customer.route("/browse", methods=['GET', 'POST'])
def browsing():
    if not current_user.is_authenticated:
        flash('Please Login.','danger')
        return redirect(url_for('Login.login'))
    cont = cont_all()
    cont_list = []
    for j in range(len(cont)):
        this_list = list(cont[j])
        cont_list.append(this_list)
    
    for n in range(len(cont_list)):
        for i in range(len(cont_list[0])):
            if cont_list[n][i] == True : 
                cont_list[n][i] = 'has'
            elif cont_list[n][i] == False: 
                cont_list[n][i] = 'does not have'
            
    

    return render_template('browse.html', title = 'Browsing', Conts = cont_list)


@Customer.route("/account", methods=['GET', 'POST'])
def account():
    if not current_user.is_authenticated:
        flash('Please Login.','danger')
        return redirect(url_for('Login.login'))
    user = current_user
    print(current_user)
    j = ' '
    for i in range(len(current_user[6])): 
        j = j + '*'
    
    

    return render_template('account.html', title = 'Account', info = user, password = j)

@Customer.route("/About", methods=['GET', 'POST'])
def About():
    if not current_user.is_authenticated:
        flash('Please Login.','danger')
        return redirect(url_for('Login.login'))

    return render_template('about.html', title = 'About')