from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class login_form(FlaskForm):
    api_key =StringField("Please enter your API_Key")
    api_secret = StringField("Please enter your API_Secret")
    submit = SubmitField("I want to be a Winner")