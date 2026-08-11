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

def add_students(name, grade, gpa):
    """
    inserting student details to table students
    """
    cursor.execute(
        "INSERT INTO students(name, grade, gpa) VALUES(?,?,?)", (name, grade, gpa),
    
    )
    connection.commit
def get_all_students():
    """
    reading tables entries
    """
    cursor.execute(""" SELECT * FROM students
    """)
    return cursor.fetchall()

def get_students_by_id(student_id):
    cursor.execute(
        """ SELECT * FROM students WHERE id = ?""", (student_id,),

    )
    return cursor.fetchone()
def update_student_gpa(student_id, new_gpa):
    cursor.execute("UPDATE students SET gpa = ? WHERE id = ?", (new_gpa, student_id),
                   )
    connection.commit()
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,),
                   )
    connection.commit()
def display_all():
     for row in get_all_students():
            print(f"id: {row[0]} name: {row[1]} grade: {row[2]}, gpa: {row[3]} ")



def main():
    students = [
        ("James", "A-", 3.75),
        ("David", "A", 4),
        ("Susan", "B", 3),
        ("Van Persie", "B+", 3.5)
    ]
    # for student in students:
    #     add_students(*student)
    print("=========== STUDENT DATA BASE =========")
    display_all()
   
    update_student_gpa(3, 3.2)
    delete_student(4)
    print("====== AFTER UPDATE =======")
    display_all()

if __name__ == "__main__":
    main()

