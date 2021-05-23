from flask import Flask, render_template, redirect, url_for, render_template, request, session, flash
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = "jsad;fk039u2401u90n3k;alkm092uqio234n92837498hwhofiuahsdf"
# client = Client(config.api_key, config.api_secret, tld = 'us')
    
if __name__ == "__main__":
        app.run(debug=True) #This will allows us to not have to rerun flask each time we make a change, it will automatically update our code. We can just hit refresh on the page to see new changes.

# Putting a parameter of debug=True in app.run() will automatically put our flask in debug mode and automatically update any changes we make to flask
    
# The Post and GET method will allow us to retrieve information from the page
@app.route('/', methods=["POST", "GET"])
def login():

# Grabbing user input from login page to validate client keys 
    if request.method == "POST":
        key = request.form["key"]
        session["key"] = key
        secret = request.form["secret"]
        session["secret"] = secret    

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

        prices = client.get_all_tickers()[ :len(balances)]
        current_prices = prices[0]['price']
        
        session["available_to_trade"] = available_to_trade
        session["balances"] = balances
        session["prices"] = prices
        session["symbols"] = symbols

# Testing that my key is validated to return my available balance to trade
        # print(session["balances"])
        # print(current_prices)

# Once the keys are validated user is allowed into home page
        return render_template('index.html', my_balances=balances, available_to_trade=available_to_trade, prices=prices, symbols=symbols)

# If the incorrect keys and secret were entered into the form, the user will not be allowed into the home page
    else: 
        return render_template("login.html")

# Route where our main page is located
@app.route('/index', methods=["POST", "GET"])
def index():
    return render_template('index.html')

# Under construction
@app.route("/logout")
def logout():
    session.pop("key", None)
    return redirect(url_for("login"))

# Route where our Binance buy method is housed
@app.route('/buy', methods=["POST","GET"])
def buy():

        # If a Post request was submitted through the buy form the following will code the Buy operation
        if request.method == "POST":
                try:
                
                        # Utilizing session to make key accessible to the buy route, to enable user to make a trade via binance
                        key = session["key"]
                        secret = session["secret"]
                        client = Client(key, secret, tld = 'us')
                        
                        # Function to make an trade 
                        order = client.create_order(symbol=request.form['symbol'],
                        side=SIDE_BUY,
                        type=ORDER_TYPE_MARKET,
                        quantity= float(request.form['quantity']))

                        #Connecting to user's binance account to retrieve information about account balances 
                        exchange_info = client.get_exchange_info()
                        info = client.get_account()
                        balances = info['balances']
                        available_to_trade = info['balances'][2]['free']

                        # Retrieve which symbol is selected for buying
                        symbols = exchange_info['symbols']

                        # Displays the current prices of Crypto currencies
                        prices = client.get_all_tickers()
                
                except Exception as e:
                        flash(e.message, "error")

                # Once the order executes, the page refreshes and updates the available balance to trade, current holdings, and prices of crypto currencies
                return render_template('index.html', my_balances=balances, available_to_trade=available_to_trade, 
                prices=prices, symbols=symbols)     
        else: 
                # If a trade has not been successfully executed the user is returned the same page
                return render_template("login.html")  
        
# Route where our Binance sell method is housed
@app.route('/sell', methods=["POST","GET"])
def sell():

        # If a Post request was submitted through the sell form the following will code will execute
        if request.method == "POST":

                # Utilizing session to make key accessible to the sell route, to enable user to make a trade via binance
                key = session["key"]
                secret = session["secret"]
                client = Client(key, secret, tld = 'us')
                
                # Function to make a sell 
                order = client.create_order(symbol=request.form['symbol'],
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity= float(request.form['quantity']))

                # Once a sell order has been successfully executed, the users available balance is retrieved to be displayed on the page
                exchange_info = client.get_exchange_info()
                info = client.get_account()
                
                balances = info['balances']
                available_to_trade = info['balances'][2]['free']
                symbols = exchange_info['symbols']

                # Displays the current prices of the Crypto currencys
                prices = client.get_all_tickers()

                # Test to see if this route is functioning properly
                # print(request.form)

                # Once the order executes, the page refreshes and updates the available balance to trade, current holdings, and prices of crypto currencies
                return render_template('index.html', my_balances=balances, available_to_trade=available_to_trade, prices=prices, symbols=symbols)       

        else: 
                # If a trade is unsuccessful it refreshes back to the same page
                return render_template("index.html")  

# Under construction, this will house the function that will allow a user to set parameters for the bot to trade
@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history', methods=["POST", "GET"])
def history():
    return render_template('history.html')

