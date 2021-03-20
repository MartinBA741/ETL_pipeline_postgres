#%% DROP TABLES

songplay_table_drop = "DROP table songplay_table"
user_table_drop = "DROP table user_table"
song_table_drop = "DROP table song_table"
artist_table_drop = "DROP table artist_table"
time_table_drop = "DROP table time_table"

#%% CREATE TABLES
# Fact table
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table (
    songplay_id int, 
    start_time datetime, 
    user_id int, 
    level int, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar, 
    user_agent varchar);
""")

#%% Dimension tables
user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table (
    user_id int, 
    first_name varchar,
    last_name varchar, 
    gender varchar, 
    level int);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table (
    song_id varchar, 
    title varchar, 
    artist_id varchar, 
    year int, 
    duration float);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table (
    artist_id varchar, 
    name varchar, 
    location varchar, 
    latitude varchar, 
    longitude varchar); 
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table (
    start_time datetime, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday varchar); 
""")

#%% INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

#%% FIND SONGS

song_select = ("""
""")

#%% QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]