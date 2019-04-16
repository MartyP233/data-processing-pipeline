# DROP TABLES

# Tables are dropped as part of the create_tables.py process.

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES
# Tables are created as part of the create_tables.py process.

# Create songplay table
songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY
                                    ,start_time date NOT NULL
                                    ,user_id int NOT NULL
                                    ,level text
                                    ,song_id text
                                    ,artist_id text
                                    ,session_id int
                                    ,location text
                                    ,user_agent text);
""")

# Create users table
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY
                                ,first_name text
                                ,last_name text
                                ,gender VARCHAR(1)
                                ,level text);
""")

# Create songs table
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id text PRIMARY KEY
                                ,title text
                                ,artist_id text
                                ,year int
                                ,duration float);
""")

# Crate artists table
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id text PRIMARY KEY
                                    ,name text
                                    ,location text
                                    ,lattitude float
                                    ,longitude float);
""")

# Create time table
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time text PRIMARY KEY
                                ,hour text
                                ,day text
                                ,week text
                                ,month text
                                ,year text
                                ,weekday text);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")

# The user table insert SQL manages conflicts by updating the row with the information from the new record
# The newest records will contain more accurate information and should take precedence.
# For example if a user changes from a free 'level' to 'paid', 'paid' should overwrite 'free'.

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT users_pkey
DO UPDATE SET level = users.level, first_name = users.first_name, 
last_name = users.last_name, gender = users.gender;
""")

# The songs table insert SQL manages conflicts by updating the row with the information from the new record
# The newest records will contain more accurate information and should take precedence.

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT songs_pkey
DO UPDATE SET title = songs.title, year = songs.year, duration = songs.duration;
""")

# The artists table insert SQL manages conflicts by updating the row with the information from the new record
# The newest records will contain more accurate information and should take precedence.

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, lattitude, longitude)
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT artists_pkey
DO UPDATE SET name = artists.name, location = artists.location, lattitude = artists.lattitude
,longitude = artists.longitude;
""")

# The time table insert SQL manages conflicts by doing nothing
# If a dupiclation of the primary key occurs, the row will be exactly the same as the existing row
# therefore there is no need to overwrite existing data, e.g. the time will be exactly the same.

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT ON CONSTRAINT time_pkey
DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT song_id, a.artist_id
FROM songs a 
LEFT JOIN artists b
    ON a.artist_id = b.artist_id
WHERE a.title = %s AND b.name = %s AND a.duration = %s
""")

# QUERY LISTS

# create list for create and drop queries

create_table_queries = [songplay_table_create, user_table_create, artist_table_create, song_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]