#Validating my client key and allow me to access Binance data stream
from binance.client import Client

#Allows me to make trades
from binance.enums import *

from flask import Flask, render_template, redirect, url_for, render_template, request
app = Flask(__name__)

if __name__ == "__main__":

# Putting a parameter of debug=True in app.run() will automatically put our flask in debug mode and automatically update any changes we make to flask
    app.run(debug=True)

# the Post and GET method will allow us to retrieve information from the page
@app.route('/', methods=["POST", "GET"])

# Utilizing request library to store information from my login form
def login():

    if request.method == "POST":
        key = request.form["key"]
        secret = request.form["secret"]

        client = Client(key, secret, tld = 'us')

        account_info = client.get_account()

        print(account_info)

        return redirect(url_for("index"))

    else: 
        return render_template("login.html")
    
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/css')
def css():
    return render_template('styles.css')

@app.route('/buy')
def buy():
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

