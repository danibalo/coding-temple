# Practice Problem: Contact Manager


Build a CRUD application for managing contacts using Python, SQLAlchemy, and SQLite.

## Contact Model

The `Contact` model includes:

- `id`: Primary key
- `first_name`: Required
- `last_name`: Required
- `email`: Required and unique
- `phone`: Optional
- `favorite`: Boolean that defaults to `False`

## Features

- Add a contact
- List all contacts sorted by last name
- Find a contact by email
- Update a contact's phone number
- Toggle a contact's favorite status
- Delete a contact

## Technologies Used

- Python
- SQLAlchemy
- SQLite

## Installation

Install SQLAlchemy:

```bash
pip install sqlalchemy
```

## Run the Program

```bash
python contact_manager.py
```

## Functions

### Add a Contact

```python
add_contact(
    "David",
    "James",
    "david24@gmail.com",
    "4088990500"
)
```

### List Contacts

```python
for contact in list_contacts():
    print(contact)
```

### Find a Contact

```python
contact = find_contact("david24@gmail.com")
print(contact)
```

### Update a Phone Number

```python
update_phone(
    "david24@gmail.com",
    "4085551234"
)
```

### Toggle Favorite Status

```python
toggle_favorite("david24@gmail.com")
```

### Delete a Contact

```python
delete_contact("david24@gmail.com")
```

## Database

The application stores contacts in a SQLite database named `contacts.db`.

The database remains saved after the program stops. Email addresses must be unique.

## Author

Created as a Python SQLAlchemy CRUD practice problem.