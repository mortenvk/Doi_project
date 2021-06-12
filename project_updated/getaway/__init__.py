from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY'] = 'egwfla78420fsjlbr892n'

db = "dbname='getaway' user='postgres' host='localhost' password = '1234' port= '5420'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'

from getaway.Login.routes import Login
from getaway.Customer.routes import Customer
app.register_blueprint(Login)
app.register_blueprint(Customer)




