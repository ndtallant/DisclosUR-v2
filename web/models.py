# models.py
from app import db

# Rather than use automap or reflections, a custom class is made
# only taking attributes that are wanted from the raw legislator
# table.
class RawLegislator(db.Model):
    '''Going to think about what I want here more.'''
    __tablename__ = 'raw_legislators'
    leg_id = db.Column(db.String, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return self.full_name


class Legislator(db.Model):
    '''Going to think about what I want here more.'''
    __tablename__ = 'legislator'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
