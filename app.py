from flask import Flask, render_template, redirect, url_for, render_template, request

app = Flask(__name__)

if __name__ == "__main__":

# Putting a parameter of debug=True in app.run() will automatically put our flask in debug mode and automatically update any changes we make to flask
    app.run(debug=True)

# the Post and GET method will allow us to retrieve information from the page
@app.route('/', methods=["POST", "GET"])
def login():

    if request.method == "POST":
        user = request.form["key"]
        pw = request.form["secret"]
        return redirect(url_for("user", usr=user))

    else: 
        return render_template("login.html")

@app.route('/<usr>', methods=["POST", "GET"])
def user(usr):
    return f"<h1>{usr}</h1>"
    
@app.route('/index', methods=["POST", "GET"])
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

