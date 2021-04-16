from templates.forms import login_form
import binance

#Validating my client key and allow me to access Binance data stream
from binance.client import Client

#Allows me to make trades
from binance.enums import *

#validating my API KEY 

#client = Client(API_Key, API_Secret, tld = 'us')

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__,)

@app.route('/index')
def index():
    return render_template('index.html')

# Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# @app.route('/')
# def login():
#     form = login_form()
#     error = None
#     if request.method == 'POST':
#         if request.form['key'] != '1234' or request.form['secret'] != 'abcd':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             #return redirect(url_for('index'))
#             print(request.form['key'])
#     return render_template('login2.html', error=error, form = form)

@app.route('/login', methods=['GET', 'POST'])
@app.route('/')
def login():
    return render_template('login2.html')
