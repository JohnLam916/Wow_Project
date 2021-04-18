from flask import Flask, render_template
app = Flask(__name__)

if __name__ == "__main__":

#   putting a parameter of debug=True in app.run() will automatically put our flask in debug mode and automatically update any changes we make to flask
    app.run(debug=True)

# the Post and GET method will allow us to retrieve information from the page
@app.route('/', methods=["POST", "GET"])
def login():
    return render_template('login.html')

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

