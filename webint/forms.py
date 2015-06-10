from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, validators


class UserRegistrationForm(Form):
    username = StringField('Your full name', [validators.Length(min=4, max=25)])
    email = StringField('Your email', [validators.Required()])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm password')
    submit = SubmitField('Register')


class LoginForm(Form):
    email = StringField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required(), ])
    submit = SubmitField('Login')
