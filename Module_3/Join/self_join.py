import sqlite3
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys=ON")
#creating employees table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
role TEXT NOT NULL,
salary INTEGER NOT NULL,
manager_id INTEGER,
FOREIGN KEY(manager_id) REFERENCES employees(id)

)
"""
)
"""
 A manager_id column in employees table (it is a foreign key referencing employees.id). Some employees are managers (their id appears as someone else's manager_id), and managers have managers too (except the top-level executive, whose manager_id is NULL).
"""
#Emplooyees data 
employees =[
    ("Susan James", "Sales Manager", 140000,None),
    ("Van Deed", "IT Manager", 200000, None),
     ("David Max", "HR Manager", 160000, None),
     ("Sara Veno", "HR Cordinator", 100000, 3),
    ("James Mask", "HR intern", 60000, 4),
    ("Olivia Cartez", "Cyber analyist", 95000, 2),
    ("Wayne Bridge", "Recruiter trainer", 120000, 3),
    ("Akuma Veno", "Data Analyst", 140000, 2),
    ("Sasha Ven", "Sales Facilitator", 110000, 1)
]
cursor.executemany(
    """INSERT INTO employees(name, role, salary, manager_id) VALUES(?,?,?,?) """, (employees),
)
cursor.execute(
    """ SELECT e.name AS employee, m.name AS manager
    FROM employees e
    LEFT JOIN employees m ON e.manager_id = m.id
"""
)
for row in cursor.fetchall():
    print(f"{row[0]} manager - {row[1]}")
