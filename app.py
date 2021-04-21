from flask import Flask, render_template, redirect, url_for, render_template, request, session, flash
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = "jsad;fk039u2401u90n3k;alkm092uqio234n92837498hwhofiuahsdf"
# client = Client(config.api_key, config.api_secret, tld = 'us')
    
if __name__ == "__main__":

    app.run(debug=True)

# Putting a parameter of debug=True in app.run() will automatically put our flask in debug mode and automatically update any changes we make to flask
    
# the Post and GET method will allow us to retrieve information from the page
@app.route('/', methods=["POST", "GET"])
def login():

# Grabbing user input from login page to validate client keys 
    if request.method == "POST":
        key = request.form["key"]
        secret = request.form["secret"]    

# Passing user input into binance validation
        client = Client(key, secret, tld = 'us')

# Testing whether the key and secret were retrieved
        # print(client, flush=True)
        # print(key, secret, flush=True)

# Retrieving client information from binance and parsing information to retrieve available balance
        exchange_info = client.get_exchange_info()
        info = client.get_account()
        balances = info['balances']
        available_to_trade = info['balances'][2]['free']

# Parsing symbols from exchange info to retrieve only crypto currency symbols
        symbols = exchange_info['symbols']

# Testing that my key is validated to return my available balance to trade
        print(available_to_trade)

# Once the keys are validated user is allowed into home page
        return render_template('index.html', my_balances=balances, available_to_trade=available_to_trade, symbols=symbols)

# If the incorrect keys and secret were entered into the form, the user will not be allowed into the home page
    else: 
        if "key" in session:
            return render_template("login.html")

@app.route('/index', methods=["POST", "GET"])
def index():

    return render_template('index.html')

@app.route("/logout")
def logout():
    session.pop("key", None)
    return redirect(url_for("login"))

@app.route('/user', methods=["POST", "GET"])
def user():
    return f"<h1></h1>"

@app.route('/buy', methods=["POST","GET"])
def buy():

# Making a market order
    try:
            order = client.create_order(symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity= request.form['quantity'])
    except Exception as e:
            flash(e.message, "error")

    return redirect(url_for('index'))

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

