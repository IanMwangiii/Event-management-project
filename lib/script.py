from event import Event
from attendee import Attendee
from tickets import Ticket

# Drop and recreate the tables
Event.drop_table()
Event.create_table()
Attendee.drop_table()
Attendee.create_table()
Ticket.drop_table()
Ticket.create_table()

# Insert some events into the table
Event.insert_event("Tech Conference", "2024-07-01 09:00:00", "San Francisco", "A conference on the latest in technology.", "2024-06-12 12:00:00")
Event.insert_event("Leadership Workshop", "2024-07-05 10:00:00", "New York", "A workshop to enhance leadership skills.", "2024-06-12 12:00:00")
Event.insert_event("Marketing Webinar", "2024-07-10 11:00:00", "Online", "A webinar on modern marketing strategies.", "2024-06-12 12:00:00")
Event.insert_event("Health Seminar", "2024-07-15 14:00:00", "Los Angeles", "A seminar on health and wellness.", "2024-06-12 12:00:00")
Event.insert_event("Business Networking Event", "2024-07-20 18:00:00", "Chicago", "An event for business networking.", "2024-06-12 12:00:00")
Event.insert_event("Automobile Trade Show", "2024-07-25 09:00:00", "Detroit", "A trade show for the latest in automobiles.", "2024-06-12 12:00:00")
Event.insert_event("Smartphone Product Launch", "2024-07-30 19:00:00", "San Francisco", "Launch event for the latest smartphone.", "2024-06-12 12:00:00")
Event.insert_event("Charity Fundraising Gala", "2024-08-01 20:00:00", "New York", "A fundraising gala for charity.", "2024-06-12 12:00:00")
Event.insert_event("Annual Corporate Meeting", "2024-08-05 09:00:00", "Boston", "Annual meeting for corporate employees.", "2024-06-12 12:00:00")
Event.insert_event("Sales Training Session", "2024-08-10 09:00:00", "Dallas", "A training session for sales teams.", "2024-06-12 12:00:00")

# Insert some attendees into the table
Attendee.insert_attendee("John Doe", "john@example.com", "1234567890", 1, "2024-06-12 12:00:00")
Attendee.insert_attendee("Alice Smith", "alice@example.com", "9876543210", 2, "2024-06-13 13:00:00")
Attendee.insert_attendee("Bob Johnson", "bob@example.com", "5555555555", 3, "2024-06-14 14:00:00")
Attendee.insert_attendee("Emily Davis", "emily@example.com", "9999999999", 1, "2024-06-15 15:00:00")
Attendee.insert_attendee("Michael Brown", "michael@example.com", "1111111111", 2, "2024-06-16 16:00:00")
Attendee.insert_attendee("Sophia Wilson", "sophia@example.com", "2222222222", 3, "2024-06-17 17:00:00")
Attendee.insert_attendee("David Martinez", "david@example.com", "3333333333", 1, "2024-06-18 18:00:00")
Attendee.insert_attendee("Emma Taylor", "emma@example.com", "4444444444", 2, "2024-06-19 19:00:00")
Attendee.insert_attendee("Daniel Anderson", "daniel@example.com", "6666666666", 3, "2024-06-20 20:00:00")
Attendee.insert_attendee("Olivia Thomas", "olivia@example.com", "7777777777", 1, "2024-06-21 21:00:00")

# Insert some tickets into the table
Ticket.insert_ticket("VIP", 100.00, 1, 1, "2024-06-12 12:00:00")
Ticket.insert_ticket("General Admission", 50.00, 2, 2, "2024-06-12 12:00:00")
Ticket.insert_ticket("VIP", 100.00, 3, 3, "2024-06-12 12:00:00")
Ticket.insert_ticket("General Admission", 50.00, 4, 1, "2024-06-12 12:00:00")
Ticket.insert_ticket("VIP", 100.00, 5, 2, "2024-06-12 12:00:00")
Ticket.insert_ticket("General Admission", 50.00, 6, 3, "2024-06-12 12:00:00")
Ticket.insert_ticket("VIP", 100.00, 7, 1, "2024-06-12 12:00:00")
Ticket.insert_ticket("General Admission", 50.00, 8, 2, "2024-06-12 12:00:00")
Ticket.insert_ticket("VIP", 100.00, 9, 3, "2024-06-12 12:00:00")
Ticket.insert_ticket("General Admission", 50.00, 10, 1, "2024-06-12 12:00:00")

# Fetch all tickets (optional)
# tickets = Ticket.fetch_all()
# print(tickets)
