from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True

@app.route('/<name>')
def index(name='Nick'):
    return 'Hello, {}'.format(name)

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/results')
def results():
    return 'This is the results page'

