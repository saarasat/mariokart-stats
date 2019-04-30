from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, validators 


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta: 
        csrf = False

class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3, max=100, message="Name must be 3-100 characters")])
    username = StringField("Username", [validators.Length(min=3, max=100, message="Username must be 3-100 characters")])
    password = PasswordField("Password", [validators.Length(min=3, max=100, message="Password must be 3-100 characters")])
    admin = BooleanField("Admin")

    class Meta:
        csfr = False