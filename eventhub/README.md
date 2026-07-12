# EventHub

Student: Darice

Project Type: Full-Stack Web Application

Framework: Django

## Description

EventHub is a web application for event management.

Users can create events, view event details, register for events and manage event participation according to their role.

## Features

### Organizer

- Create events
- View events
- Update events
- Delete events
- View attendees

### Attendee

- View events
- Register for events

## Technologies

- Python
- Django
- SQLite
- Bootstrap

## Local Installation

Clone the repository:

```bash
git clone REPOSITORY_URL
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

db.sqlite3

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

1. Login
2. Browse events
3. View event details
4. Register to an event
5. Create, update or delete events as Organizer

## Deployment

Deployment URL:

TO_BE_ADDED