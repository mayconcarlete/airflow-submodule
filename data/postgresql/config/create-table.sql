CREATE SCHEMA sample;
DROP TABLE IF EXISTS sample.input_data;
CREATE TABLE sample.input_data (
    id SERIAL PRIMARY KEY,
    input_text VARCHAR(10),
    datetime_created TIMESTAMP
);
DROP TABLE IF EXISTS sample.output_data;
CREATE TABLE sample.output_data (
    id int UNIQUE,
    event_id VARCHAR(40),
    input_text VARCHAR(10),
    processed_text VARCHAR(50),
    datetime_created TIMESTAMP,
    datetime_inserted TIMESTAMP
);