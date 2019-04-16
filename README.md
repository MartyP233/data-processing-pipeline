# Songplay analysis data pipeline

This repo contains python source and jupyter notebooks for running and testing the songplay analysis data pipeline.

## Purpose

Sparkify analysts want to analyze the data they've been collecting on songs and user activity on their new music streaming app, with a particular focus on understanding what songs users are listening to.

## Data Pipeline

The data pipeline process establishes a database and tables, processes JSON data files, and inserts processed data into those tables. 

The pipeline process 2 types of JSON data file

### Song dataset 
Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID

### Log dataset

The log datasets contain activity logs from the music streaming app, and are partitioned by year and month.

## Running the process

The process is typically run in the following order:

1. create tables.py - to reset and establish the database
2. etl.py - to process and load data
3. test.ipynb - for any manual data validation

## More detail on script files and their purpose:

### sql_queries.py 
- *contains the SQL queries that are applied in both the create_tables.py file and the etl.py file*
### create_tables.py 
- *establishes the database connection, drops and recreates the database and the tables within it*
### etl.py 
- *processes and loads json data into the database*
### etl.ipynb 
- *can be used for interactively testing parts of the etl process*
### test.ipynb 
- *contains sql queries to view data that has been inserted into tables*



