from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='confirm password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Login')


class LoginForm(FlaskForm):
    username = StringField(label='username:')
    password = PasswordField(label='password:')
    submit = SubmitField(label='Login')
