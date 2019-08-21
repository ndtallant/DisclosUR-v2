'''
    app.py
    ------

    Author: ndtallant

    Description: This file is the server logic for the website. Rather than a
    separate models file, the existing database tables are reflected to
    SQLAlchemy table ojects.

'''
from flask import Flask, render_template, url_for, session, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Reflect Tables from DB to SQLAlchemy Models
legislator = db.Table(
    'legislator', db.metadata, autoload=True, autoload_with=db.engine
)

cpi = db.Table(
    'cpi', db.metadata, autoload=True, autoload_with=db.engine
)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page of the webapp."""
    return '<h1>Hello, World!</h1>'

@app.route('/results')
def results():
    """Returns the legislators and relevant information."""
    print(db.session.query(legislator).all()[:10])
    print(db.session.query(cpi).all()[:10])
    return '<h1>Hello, Results!</h1>'

@app.route('/about')
def about():
    """Simply renders the about page."""
    return render_template('about.html')
