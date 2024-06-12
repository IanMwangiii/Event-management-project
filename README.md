# Event Management System

## Description

The Event Management System is designed to efficiently manage event-related data, attendee information, and ticket details. The system comprises three main tables: `events`, `attendees`, and `tickets`. Relationships between these tables ensure comprehensive data organization and integrity.

## Database Structure

### Events Table

Stores information about events, including:
- `id`: Primary Key
- `name`: Event name
- `date`: Event date
- `location`: Event location
- `description`: Event description
- `created_at`: Creation timestamp

### Attendees Table

Stores information about attendees, such as:
- `id`: Primary Key
- `name`: Attendee name
- `email`: Attendee email
- `phone`: Attendee phone number
- `event_id`: Foreign Key referencing `events.id`
- `created_at`: Creation timestamp

### Tickets Table

Stores details about tickets, including:
- `id`: Primary Key
- `type`: Ticket type
- `price`: Ticket price
- `attendee_id`: Foreign Key referencing `attendees.id`
- `event_id`: Foreign Key referencing `events.id`
- `created_at`: Creation timestamp

## Relationships

- **One-to-Many between Events and Attendees**: An event can have multiple attendees, but each attendee is associated with only one event.
- **One-to-Many between Attendees and Tickets**: An attendee can have multiple tickets, but each ticket is associated with only one attendee.
- **One-to-Many between Events and Tickets**: An event can have multiple tickets, but each ticket is associated with only one event.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/IanMwangiii/Phase3_final-project.git
    cd Phase3_final-project
    ```

2. Create a virtual environment and activate it:

    ```sh
    pipenv install
    pipenv shell
    ```

3. Ensure you have SQLite3 installed and configured.

## Configuration

The database configuration is handled in the `config.py` file, which sets up the connection to the SQLite database.

## Usage

1. Use the `Event`, `Attendee`, and `Ticket` classes to manage the respective tables.
2. You can create, drop, and insert records into the tables using the provided class methods.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Repository

For more information, visit the [GitHub repository](https://github.com/IanMwangiii/Phase3_final-project).

---

This `README.md` provides a clear and concise overview of the Event Management System project, including the database structure, relationships, installation and configuration instructions, and usage guidelines. It is formatted for optimal display on GitHub.# Phase-3-final-project
# Phase-3-final-project
# Event-management-project
