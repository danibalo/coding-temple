import sqlite3
"""
connecting to dabase school.db, create if not exist
"""
connection = sqlite3.Connection("school.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
#Creating table of students with id, name, grade and gpa
cursor.execute(
        """ CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade INTEGER NOT NULL,
        gpa REAL
        )
        """
    )

connection.commit()

# ===== CRUD FUNCTIONS ===

def add_student(name, grade, gpa):
    """
    inserting student details to table students
    """
    cursor.execute(
        "INSERT INTO students(name, grade, gpa) VALUES(?,?,?)", (name, grade, gpa),
    
    )
    connection.commit
    print(f"{name} was added successfully")
def get_all_students():

    cursor.execute(""" SELECT * FROM students
    """)
    return cursor.fetchall()

def get_student_by_id(student_id):
    cursor.execute(
        """ SELECT * FROM students WHERE id = ?""", (student_id,),

    )
    return cursor.fetchone()
def update_student_gpa(student_id, new_gpa):
    cursor.execute("UPDATE students SET gpa = ? WHERE id = ?", (new_gpa, student_id),
                   )
    affected_rows = cursor.rowcount
    connection.commit()
    if affected_rows == 0:
        print(f"No student found with ID {student_id}")
        return False
    print("Student GPA updated successfully")
    return True
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,),
                   )
    affected_rows = cursor.rowcount
    connection.commit()
    if affected_rows == 0:
        print(f"No student found with ID {student_id}")
        return False
    print("Student deleted successfullly")
    return True

def get_valid_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a mumber greater than or equal to {minimum}")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a number less than or equal to {maximum}.")
                continue
            return value
        except ValueError:
            print("Enter valid whole number")
def get_valid_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a mumber greater than or equal to {minimum}")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a number less than or equal to {maximum}.")
                continue
            return value
        except ValueError:
            print("Enter a valid number")
def ask_yes_or_no(response):
    while True:
        answer = input(response).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Enter y for yes n for no")
def display():
     students = get_all_students()
     if not students:
            print("No students found")
            return
     print("\n================================ STUDENT ROSTER===================")

     for student in students:
            print(f"id: {student[0]} name: {student[1]} grade: {student[2]}, gpa: {student[3]} ")
def display_menu():
        print("""
    Student Roster Manager\n
1. Add a student
2. View all students
3. Update a student's GPA
4. Delete a student
5. Quit
""")

#===========OPERATIONS=============
def add_student_menu():
    while True:
        name = input("Enter the student's name: ").strip()
        while not name:
            print("The students name can't be empty")
            name = input("Enter the student's name: ").strip()
        grade = get_valid_integer(
            "Enter student's grade",
            minimum = 0,
            maximum= 100,
        )
        gpa = get_valid_float(
            "Enter student's gpa",
            minimum = 0.0,
            maximum = 4.0,
        )
        add_student(name, grade, gpa)
        if not ask_yes_or_no("Add another student? (y/n): "):
            break
def update_student_menu():
    student_id = get_valid_integer(
        "Enter the student ID: ",
        minimum=1,

    )
    student = get_student_by_id(student_id)
    if student is None:
        print(f"No student found with ID {student_id}.")
        return
    print(
        f"Student: {student[1]} | "
        f"Current GPA: {student[3]:.2f}"
    )

    new_gpa = get_valid_float(
        "Enter the new GPA (0.0-4.0): ",
        minimum=0.0,
        maximum=4.0,
    )

    update_student_gpa(student_id, new_gpa)


def delete_student_menu():
    student_id = get_valid_integer(
        "Enter the student ID: ",
        minimum=1,
    )

    student = get_student_by_id(student_id)

    if student is None:
        print(f"No student found with ID {student_id}.")
        return

    print(
        f"Student: {student[1]} | "
        f"Grade: {student[2]} | "
        f"GPA: {student[3]:.2f}"
    )

    confirm = ask_yes_or_no(
        f"Delete {student[1]}? (y/n): "
    )

    if confirm:
        delete_student(student_id)
    else:
        print("Deletion cancelled.")


# ---------------- MAIN PROGRAM ----------------


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            display()

        elif choice == "3":
            update_student_menu()

        elif choice == "4":
            delete_student_menu()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    finally:
        connection.close()



