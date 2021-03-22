# ETL_pipeline_postgres
In this project, I've created a data model with Postgres and build an ETL pipeline for the fictive startup called Sparkify.
The ETL Pipline reads in json files on user activity and metadata on songs and transform it before loading it to a postgres STAR schema database. 

## Run the code by:
1) create_tables.py - This will create tables (and drop if any exists first) 
2) etl.py - This will read and process files from the metadata and useractivity files stored in the data folder.

To test and explore the output, feel free to explore the jupyter notebooks: test and etl.