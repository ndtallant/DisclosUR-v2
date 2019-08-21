# models.py

from app import db

class Legislator(db.Model):
    '''Going to think about what I want here more.'''
    __tablename__ = 'legislator'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
