import sqlite3

# Establish connection to the database
conn = sqlite3.connect("db/events.db")

cursor = conn.cursor()
