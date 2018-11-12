#!/usr/bin/env python
'''
districts.py

'''
import pandas as pd

data = {}

def get_district(i):
    '''
    Gets the district csv file from census,
    adds data to global dict.
    '''
    n = '0' + str(i) if i < 10 else str(i)
    data[n] = pd.read_table('https://www2.census.gov/geo/relfiles/cdsld13/'+
                            '{}/co_cd_delim_{}.txt'.format(n, n)
                            , skiprows=1
                            , sep=','
                            , dtype={'State': str
                                   , 'County': str
                                   , 'CongressionalDistrict': str})
for i in range(1, 56):
    try:
        get_district(i)
    except:
        continue

districts = pd.concat(data)
fips = pd.read_table('https://www2.census.gov/geo/docs/reference/codes/'+
                     'files/national_county.txt'
                    , sep=','
                    , header=None
                    , names=['state_postal'
                           , 'statefp'
                           , 'countyfp'
                           , 'county'
                           , 'classfp']
                    , dtype={'state_postal': str
                           , 'statefp': str
                           , 'countyfp': str
                           , 'county': str
                           , 'classfp': str})
fips.merge(districts
        , how='left'
        , left_on=['statefp', 'countyfp']
        , right_on=['State', 'County'])

fips.to_csv('../data/districts_by_county.csv', index=False)
