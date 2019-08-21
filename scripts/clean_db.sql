DROP TABLE IF EXISTS legislator;
CREATE TABLE legislator AS
    SELECT
        full_name,
        lower(full_name) as fuzzy_name,
        upper(state) AS state,
        chamber,
        district,
        CASE WHEN party IN ('Progressive', 'Democratic/Progressive', 'Progressive/Democratic', 
                            'Democratic', 'Democratic-Farmer-Labor') THEN 'D'
             WHEN party IN ('Republican', 'Libertarian') THEN 'R'
             WHEN party IN ('Independent', 'Nonpartisan') THEN 'I'
             ELSE NULL END AS cleaned_party,
        photo_url
    FROM 
        raw_legislators
    WHERE
        cleaned_party IS NOT NULL
      AND
        state IS NOT NULL;

/* CPI Creation, Note: || is the concatenation operator in SQLite */
DROP TABLE IF EXISTS cpi;
CREATE TABLE cpi AS
SELECT 
    lower(substr(lawmaker, position + 2) || " " || substr(lawmaker, 1, position - 1)) AS fuzzy_name,
    state,
    body,
    district,
    replace(employer_business_interest, "'", '') AS interest, 
    /*CASE WHEN employer_business_interest LIKE '%BRAMBLE%'
        THEN 'BRAMBLE & COMPANY - CPA' ELSE employer_business_interest 
    END AS employer_business_interest,*/
    industry,
    disclosure_report 
FROM (
    SELECT *, instr(lawmaker, ',') AS position
    FROM raw_cpi 
);
