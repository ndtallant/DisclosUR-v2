/*
    create_db.sql
    -------------

    Author: ndtallant
    Description: This file creates the database for Open States and CPI data.
*/

/* Open States */
DROP TABLE IF EXISTS raw_legislators;
CREATE TABLE raw_legislators (
    leg_id INT NOT NULL,
    full_name VARCHAR NOT NULL,
    first_name VARCHAR,
    middle_name VARCHAR,
    last_name VARCHAR NOT NULL,
    suffixes VARCHAR,
    nickname VARCHAR,
    active BOOLEAN NOT NULL,
    state VARCHAR NOT NULL,
    chamber VARCHAR,
    district VARCHAR,
    party VARCHAR,
    photo_url VARCHAR,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

/* SQLite Meta */
.mode csv
.import ../data/open_states.csv raw_legislators
.exit
