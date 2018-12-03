DisclosUR
=========

DisclosUR-v2 is an end to end data product exploring financial disclosures for US legislators at the state level and their relation to corporate entities.

## Data Sources

#### Open States

Open States ([site](https://openstates.org/)) is an open source project and collection of tools that allow everyday people to track information about their representatives. This project uses Open States as the base data source for identifying legislators by location and linking them to financial disclorures published by the Center for Public Integrity.

#### Center for Public Integrity (CPI)

The Center for Public Integrity describes itself as an "investigative news organization that gives voice to the public and sparks change by going behind closed doors to reveal abuses of power in Washington". The organization uses to technology to pursue data-driven independent reporting seeking transparency, accountability and efficiency in our government. This project uses their [2015 dataset](https://github.com/PublicI/state-lawmakers-disclosures) of state lawmaker disclosures.

#### Open Corporates

OpenCorporates is the largest open database of companies and company data in the world. This project uses their [API](https://api.opencorporates.com/) to link possible corporate entities to legislators.

## Limitations

The current implementation of this project links legislator data from 2017 to financial disclosure data from 2015. Although many legislators continued from 2015 to 2017, there will be gaps created from this disparity.

## Usage


Contribute
----------
- [Issue Tracker](https://github.com/ndtallant/DisclosUR_v2/issues)
- [Source Code](https://github.com/ndtallant/DisclosUR_v2)
