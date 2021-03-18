["num_songs", "artist_id", "artist_latitude", "artist_longitude", "artist_location", "artist_name","song_id","title","duration","year"]

# DROP TABLES

songplay_table_drop = "DROP table songplay_table"
user_table_drop = ""
song_table_drop = ""
artist_table_drop = ""
time_table_drop = ""

# CREATE TABLES

# Fact table
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay_table (
    songplay_id, 
    start_time, 
    user_id int, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent);
""")

# Dimension tables
user_table_create = ("""
CREATE TABLE IF NOT EXISTS user_table (user_id, first_name, last_name, gender, level);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song_table (song_id, title, artist_id, year, duration);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist_table (artist_id, name, location, latitude, longitude); 
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table (start_time, hour, day, week, month, year, weekday); 
""")

# INSERT RECORDS

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

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]