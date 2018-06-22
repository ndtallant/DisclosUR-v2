'''
This file contains classes for:

    Legislator
    FinancialInterest

This project uses these classes to enclose relevant data
and pass it through to templates.
'''

class Legislator:
    def __init__(self, party, name, first, last, os_id, district, 
                 active, state, email, photo_url, url, chamber, offices):
       '''Legislator Class''' 
       self.party = party    
       self.name = name #full_name
       self.last = last #last_name 
       self.first = first #first_name 
       self.os_id = os_id # just id through API
       self.district = district 
       self.state = state
       self.email = email 
       #'leg_id' how is this different from id? 
       self.in_office = active
       self.photo_url = photo_url
       # roles notate examples 
       self.url = url # see if these are legit
       self.chamber = chamber 
       self.offices # check this too

    def __str__(self):
        return (f'{self.name} ({self.party}), '
                f'{self.district} District of {self.state}')

class FinancialInterest:
    pass
