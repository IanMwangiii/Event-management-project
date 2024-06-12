# config.py
import sqlite3

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# attendee.py
from config import conn, cursor

class Attendee:
    def __init__(self, id, name, email, phone, event_id):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.event_id = event_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS attendees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            email VARCHAR,
            phone VARCHAR,
            event_id INTEGER,
            FOREIGN KEY (event_id) REFERENCES events(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS attendees;
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def insert_attendee(cls, name, email, phone, event_id, created_at):
        sql = """
            INSERT INTO attendees (name, email, phone, event_id) VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (name, email, phone, event_id))
        conn.commit()
