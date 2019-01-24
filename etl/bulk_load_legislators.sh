# Runs \copy for each <st>_legislators.csv file in data/

for state in $(cat states.txt); do
    csv_file=`echo "data/${state}_legislators.csv"`
    psql disclosur -c "\copy raw_data.legislator FROM '${csv_file}' WITH CSV HEADER;"
done
