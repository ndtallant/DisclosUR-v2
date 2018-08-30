# About DisclosUR

Financial disclosures for US legislators at the state level and their relation to corporate entities.

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

## Contribute

[Issue Tracker](https://github.com/ndtallant/DisclosUR_v2/issues) | 
[Source Code](https://github.com/ndtallant/DisclosUR_v2)

