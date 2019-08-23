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

from models import Legislator, Interest

# Reflect Tables from DB to SQLAlchemy Models
#cpi = db.Table(
#    'cpi', db.metadata, autoload=True, autoload_with=db.engine
#)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Home page of the webapp."""
    return render_template('index.html')

@app.route('/results')
def results():
    """Returns the legislators and relevant information."""
    legislators = Legislator.query.all()[:20]
    for legislator in legislators:
        print(legislator.full_name, legislator.interest)
    return render_template('results.html', legislators=legislators)

@app.route('/about')
def about():
    """Simply renders the about page."""
    return render_template('about.html')
