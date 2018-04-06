from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bootstrap')
def boot():
    return render_template('bootstrap.html')

@app.route('/results', methods=['POST'])
def results():
    address = request.form['user_address'] 
    return 'The user address is {}'.format(address)

@app.route('/about')
def about():
    return 'This is the about page'
