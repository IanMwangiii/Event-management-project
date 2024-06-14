def print_help():
    print("Welcome to Event Management CLI!")
    print("Available actions:")
    print("  init          : Initialize the database and create tables.")
    print("  drop          : Drop all tables from the database.")
    print("  add_event     : Add a new event to the database.")
    print("  add_attendee  : Add a new attendee to an event.")
    print("  add_ticket    : Add a new ticket to an event.")
    print("  list_events   : List all events.")
    print("  list_attendees: List all attendees.")
    print("  list_tickets  : List all tickets.")
    print("Usage:")
    print("  python3 help.py   : Display this help message.")

if __name__ == "__main__":
    print_help()
