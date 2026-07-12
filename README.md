# EventHub

EventHub is a Django web application that allows organizers to create and manage events and attendees to register for them.

## Features

### Organizer

- Create events
- Edit events
- Delete events
- View event details
- Manage events

### Attendee

- Login
- Browse events
- View event details
- Register for events

## Technologies

- Python
- Django
- SQLite
- Bootstrap

## Local Installation

Clone the repository:

```bash
git clone https://github.com/dariceLorinda/EventHub.git
cd EventHub
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run server:

```bash
python manage.py runserver
```

## Database

The project includes a pre-populated SQLite database:

```text
db.sqlite3
```

## Demo Accounts

### Organizer

Username: organizer_demo

Password: organizer123

Role: Organizer

### Attendee

Username: attendee_demo

Password: attendee123

Role: Attendee

## Main Workflow

1. Login with one of the demo accounts.
2. Browse available events.
3. View event details.
4. Register for an event.
5. Create, edit and delete events as Organizer.

## Project Structure

```text
EventHub/
│
├── events/
├── users/
├── templates/
├── db.sqlite3
├── requirements.txt
├── manage.py
└── README.md
```

## Deployment

This project was developed and tested locally using Django and SQLite.

No public deployment URL is available.

## Author

Darice Lorinda Dezo Simo

University of Florence

Multimedia Project – EventHub

