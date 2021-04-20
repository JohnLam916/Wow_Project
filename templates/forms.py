from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    api_key = StringField('Please enter your api_key', validators=[DataRequired()])
    api_secret = PasswordField('Please enter your api_secret', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('I want to be a Winner')
