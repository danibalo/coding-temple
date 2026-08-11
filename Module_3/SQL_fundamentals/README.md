# Student Roster CRUD

## Objective

This project implements a complete CRUD application for managing a student roster with Python and SQLite.

## Project Requirements

### Project Files

The project includes:

- `student_roster.py` — contains the Python code
- `school.db` — stores the student records

### Database Structure

The `students` table contains:

- `id` — primary key, autoincrement
- `name` — text, not null
- `grade` — text, not null
- `gpa` — real

### CRUD Operations

The application provides the following functions:

- `add_student(name, grade, gpa)` — adds a student
- `get_all_students()` — returns all students
- `get_student_by_id(student_id)` — returns a student by ID
- `update_student_gpa(student_id, new_gpa)` — updates a student's GPA
- `delete_student(student_id)` — deletes a student

## Program Demonstration

The main program:

- Adds at least four students
- Displays all students
- Retrieves a student by ID
- Updates one student's GPA
- Deletes one student
- Displays the remaining students

## Running the Program

```bash
python student_roster.py