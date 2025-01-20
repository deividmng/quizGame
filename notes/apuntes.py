# Python - SQLite Example

# ! Import SQLite

# * We import "sqlite3" as "sql" so that we can use "sql" as our reference
import sqlite3 as sql

# ! Connect to the Database

# * The "connection" variable is using the "connect" method from sqlite in order to establish a connection to the specified DB in our case "movies.db" if the DB does not exist it will create one with the name supplied
connection = sql.connect("movies.db")

# ! Create cursor object

# * We create a "cursor" variable in order to execute SQL commands via Python - Think of the cursor as our accesspoint to SQL
cursor = connection.cursor()

# ! Use the cursor to run an SQL command
# * We pass our SQL commmand as an argument to our "cursor.execute()" method. 
# * If you contain your SQL code between 2 sets of 3 quotes you can write SQL commands to be applied to the database """SQL CODE"""

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,   
        title TEXT,               
        genre TEXT,               
        director TEXT,            
        release_year INTEGER      
    )
""")

# ! Commiting Changes to the DB - Only required when, Creating data, Updating data or Deleting data. Not required if reading only

# * By using the "commit()" method it commits our changes
connection.commit()

# ! Insert a record via a python function
def add_movie(title, genre, director, release_year):
    cursor.execute("""
        INSERT INTO movies (title, genre, director, release_year)
        VALUES (?, ?, ?, ?)
        """, (title, genre, director, release_year))
    connection.commit()

add_movie("Oppenheimer", "Drama", "Christopher Nolan", 2023)

