from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email



class RegForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    likes_heat = BooleanField('I like hot weather')
    plane_pref = BooleanField('I prefer travel by plane')
    boat_pref = BooleanField('I prefer travel by boat')
    train_pref = BooleanField('I prefer travel by train')
    budget = IntegerField('What is your budget (DKK)?',
                            validators=[DataRequired()]) 
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')