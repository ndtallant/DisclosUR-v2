# models.py

import datetime
from app import db

class Legislator(db.Model):
    '''Going to think about what I want here more.'''
    __tablename__ = 'legislator'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text):
        self.text = text
        self.date_posted = datetime.datetime.now()
