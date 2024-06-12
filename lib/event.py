from config import cursor, conn

class Event:
    def __init__(self, id, name, date, location, description, created_at):
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.description = description
        self.created_at = created_at

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            date TIMESTAMP,
            location VARCHAR,
            description TEXT,
            created_at TIMESTAMP
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS events;
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def insert_event(cls, name, date, location, description, created_at):
        sql = """
            INSERT INTO events (name, date, location, description, created_at) VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (name, date, location, description, created_at))
        conn.commit()
