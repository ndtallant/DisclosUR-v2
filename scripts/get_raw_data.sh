# This script collects raw data for Open States and CPI

mkdir data
mkdir data/zips

# Collect Open States Data
for state in `cat states.txt`; do 
    curl -s "https://data.openstates.org/legacy/csv/${state}.zip" -o "data/zips/${state}.zip";
    unzip data/zips/${state}.zip ${state}_legislators.csv -d data;
done;

# Stack states together into one dataset
csvstack data/*_legislators.csv > data/open_states.csv

# Clean up
rm -rf data/zips
rm data/*_legislators.csv

# Collect Center for Public Integrity Data
curl -s https://raw.githubusercontent.com/PublicI/state-lawmakers-disclosures/master/lawmakers.csv -o data/cpi.csv

# Pesky ASCII codes
# TODO: Fix the sed/gsed on OSX debacle... maybe in docker...
vim -c ':%s/\%x92//g' -c ':x' data/cpi.csv 
