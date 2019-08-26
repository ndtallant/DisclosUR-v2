from app import db

# Rather than use automap or reflections, a custom class is made
# only taking attributes that are wanted from the raw legislator
# table.

class Legislator(db.Model):
    '''Going to think about what I want here more.'''
    __tablename__ = 'legislator'

    full_name = db.Column(db.String, primary_key=True)
    fuzzy_name = db.Column(db.String, nullable=True)
    cleaned_party = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String)
    interests = db.relationship('Interest', backref='cpi')


class Interest(db.Model):
    '''Going to think about what I want here more.'''
    __tablename__ = 'cpi'

    fuzzy_name = db.Column(db.String, db.ForeignKey('legislator.fuzzy_name'),
            primary_key=True)
    state = db.Column(db.String, nullable=False)
    district = db.Column(db.String, nullable=False)
    disclosure_report = db.Column(db.String)

    def __repr__(self):
        return self.disclosure_report
