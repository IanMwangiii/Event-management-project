from config import cursor, conn

class Ticket:
    def __init__(self, id, type, price, attendee_id, event_id, created_at):
        self.id = id
        self.type = type
        self.price = price
        self.attendee_id = attendee_id
        self.event_id = event_id
        self.created_at = created_at

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type VARCHAR,
            price DECIMAL,
            attendee_id INTEGER,
            event_id INTEGER,
            created_at TIMESTAMP,
            FOREIGN KEY (attendee_id) REFERENCES attendees(id),
            FOREIGN KEY (event_id) REFERENCES events(id)
            )
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS tickets;
        """
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def insert_ticket(cls, type, price, attendee_id, event_id, created_at):
        sql = """
            INSERT INTO tickets (type, price, attendee_id, event_id, created_at) VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (type, price, attendee_id, event_id, created_at))
        conn.commit()
    @classmethod
    def fetch_all(cls):
        cursor.execute("SELECT * FROM tickets")
        return cursor.fetchall()