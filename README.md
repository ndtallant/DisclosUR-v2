DisclosUR
=========

Financial disclosures for US legislators at the state level and their relation to corporate entities.

## Installation
Install dependent packages by running:

```
pip3 install -r requirements.txt
```

from the top level directory - we recommend using a virtual environment. To populate the database, please see 'Populating the database' under 'Usage'.

## Required Modules

* [pyopenstates](http://docs.openstates.org/projects/pyopenstates/en/latest/pyopenstates%20module.html)
* [requests](http://docs.python-requests.org/en/master/)
* [json](https://docs.python.org/3/library/json.html)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [re](https://docs.python.org/3/library/re.html)
* [django](https://www.djangoproject.com/)
* [django-tables2](http://django-tables2.readthedocs.io/en/latest/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [pandas](https://pandas.pydata.org/)
* [tableau](https://onlinehelp.tableau.com/current/pro/desktop/en-us/embed.html)

## Data Sources & APIs

### Open States
An organization and suite of tools to collect data on bills, legislators, committees, and events. We interacted with this data using the python API listed above, and through using [their website](https://openstates.org/).

### Center for Public Integrity (CPI)
Data-driven independent reporting since 1989. CPI  believes "in the democratic process and seek transparency, accountability and efficiency in our government." Data for this project comes from their Conflicted Interests project:
https://github.com/PublicI/state-lawmakers-disclosures

### Open Corporates
The largest open database on companies in the world. Their goal is to "make information on companies more usable and more widely available for the public benefit, particularly to tackle the use of companies for criminal or anti-social purposes, for example corruption, money laundering and organised crime". Their information is sourced from publicly available official company registries.

Documentation for the API:
https://api.opencorporates.com/documentation/API-Reference

## Project / Data Limitations

While the data from Open States is from 2017, the data from CPI is from 2015. This may leave some lacking results when the user searches for a legislator that was not in office in 2015. Furthermore, legislators that are not currently in office may not have appropriate information about their political party. Because the CPI database does not include official company registry numbers for legislator's business / employment interests, we cannot guarantee that name-matches in the OpenCorporates database are in fact the same entity. 

## Data Visualization
Made connections to CPI data source and created dynamic data visualizations using Tableau.  Hosted dynamic data visualizations on Tableau's public server [here](https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/CPIDataViz/Dashboard1) and [here](https://public.tableau.com/profile/saptarshi.ghose#!/vizhome/cs_map_final/Sheet1) and used HTML embedding to incorporate data visualizations into our website.  

## Usage

### Populating the database
If you have a demo of this project on a flashdrive, this is unnecessary.

Have a file `.env`, in the `site_container` directory with the google maps, open states, and open corporates API keys. (The local demo on a flash drive has this already).

In the `site_container` directory, run `repopulate`. This will reset the django database with lawmakers pandas financial interests. It should take about 2 minutes to run.

Run `populate_open_corps.py`. This may take some time depending on the internet connection.

Contribute
---------

- Issue Tracker: https://github.com/ndtallant/DisclosUR_v2/issues
- Source Code: https://github.com/ndtallant/DisclosUR_v2

