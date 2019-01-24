/* This file creates schemas for the
   existing postgres database: disclosur

   Populating the tables occurs in <>
*/

DROP SCHEMA IF EXISTS raw_data CASCADE;
CREATE SCHEMA raw_data;

CREATE TABLE raw_data.legislator (
	leg_id VARCHAR NOT NULL, 
	full_name VARCHAR, 
	first_name VARCHAR, 
	middle_name VARCHAR, 
	last_name VARCHAR, 
	suffixes VARCHAR, 
	nickname VARCHAR, 
	active BOOLEAN, 
	state VARCHAR, 
	chamber VARCHAR, 
	district VARCHAR, 
	party VARCHAR, 
	photo_url VARCHAR, 
	created_at TIMESTAMP WITHOUT TIME ZONE, 
	updated_at TIMESTAMP WITHOUT TIME ZONE
);

DROP SCHEMA IF EXISTS web_app CASCADE;
CREATE SCHEMA web_app;

CREATE TABLE web_app.legislator (
	leg_id VARCHAR NOT NULL, 
	full_name VARCHAR NOT NULL, 
	state VARCHAR NOT NULL, 
	chamber VARCHAR, 
	district VARCHAR NOT NULL, 
	party VARCHAR, 
	photo_url VARCHAR 
);
