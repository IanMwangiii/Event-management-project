import argparse
from event import Event
from lib.attendee import Attendee
from lib.tickets import Ticket

def initialize_db():
    Event.create_table()
    Attendee.create_table()
    Ticket.create_table()
    print("Database and tables created.")

def drop_db():
    Event.drop_table()
    Attendee.drop_table()
    Ticket.drop_table()
    print("Tables dropped.")

def add_event():
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD HH:MM:SS): ")
    location = input("Enter event location: ")
    description = input("Enter event description: ")
    created_at = input("Enter creation timestamp (YYYY-MM-DD HH:MM:SS): ")
    Event.insert_event(name, date, location, description, created_at)
    print(f"Event '{name}' added.")

def add_attendee():
    name = input("Enter attendee name: ")
    email = input("Enter attendee email: ")
    phone = input("Enter attendee phone: ")
    event_id = int(input("Enter event ID: "))
    created_at = input("Enter creation timestamp (YYYY-MM-DD HH:MM:SS): ")
    Attendee.insert_attendee(name, email, phone, event_id, created_at)
    print(f"Attendee '{name}' added.")

def add_ticket():
    type = input("Enter ticket type (e.g., VIP, General Admission): ")
    price = float(input("Enter ticket price: "))
    attendee_id = int(input("Enter attendee ID: "))
    event_id = int(input("Enter event ID: "))
    created_at = input("Enter creation timestamp (YYYY-MM-DD HH:MM:SS): ")
    Ticket.insert_ticket(type, price, attendee_id, event_id, created_at)
    print(f"Ticket '{type}' added.")

def main():
    parser = argparse.ArgumentParser(description="Manage events, attendees, and tickets.")
    parser.add_argument('action', choices=['init', 'drop', 'add_event', 'add_attendee', 'add_ticket'], help="Action to perform")

    args = parser.parse_args()

    if args.action == 'init':
        initialize_db()
    elif args.action == 'drop':
        drop_db()
    elif args.action == 'add_event':
        add_event()
    elif args.action == 'add_attendee':
        add_attendee()
    elif args.action == 'add_ticket':
        add_ticket()

if __name__ == "__main__":
    main()
