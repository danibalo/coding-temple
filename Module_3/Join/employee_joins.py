import sqlite3
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys=ON")
#creating department table
cursor.execute(
    """ CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL)
"""
)
#creating employees table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
role TEXT NOT NULL,
salary INTEGER NOT NULL,
department_id INTEGER,
FOREIGN KEY(department_id) REFERENCES departments(id)

)
"""
)
#Creating Projects table
cursor.execute(
    """ CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    employee_id INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employees(id)
    )
""")

#Department datas
departments = [
    ("Sales", "Miami, Florida"),
    ("HR", "Atlanta, Georgia"),
    ("IT", "New York")
]
cursor.executemany(
    """ INSERT INTO departments(name, location) VALUES (?,?)""", (departments),)

#Emplooyees data 
employees =[
    ("Susan James", "Sales Manager", 140000, 1),
    ("James Mask", "HR intern", 60000, 2),
    ("Olivia Cartez", "Cyber analyist", 95000, 3),
    ("Sara Veno", "HR Cordinator", 100000, 2),
    ("Wayne Bridge", "Recruiter trainer", 120000, 2),
    ("David Max", "HR Manager", 160000, 2),
    ("Akuma Veno", "Data Analyst", 140000, 3),
    ("Sasha Ven", "Sales Facilitator", 110000, 1)
]
cursor.executemany(
    """INSERT INTO employees(name, role, salary, department_id) VALUES(?,?,?,?) """, (employees),
)
#Projects available
projects = [
    ("Talent coach", 1),
    ("Application Development", 7),
    ("University Talent finder", 4),
    ("Social Media", 5)
] 
cursor.executemany(
    """INSERT INTO projects(title, employee_id) VALUES(?,?) 
""", (projects))

print("Tables are created, and populated")

# Query 1: List all employees with their department name 
cursor.execute("""
SELECT e.name, d.name
FROM employees e
JOIN departments d on e.department_id = d.id
ORDER BY e.name 
""")
print("Query 1")
for row in cursor.fetchall():
    print(f"{row[0]} -> {row[1]}")
# Query 2: List all departments, even those with no employees.
cursor.execute("""
SELECT DISTINCT d.name 
FROM departments d
LEFT JOIN employees e on d.id = e.department_id
ORDER BY d.name
""")
print("\nQUERY 2")
for row in cursor.fetchall():
    print(f"{row[0]}")
# Query 3: List all employees and the projects they lead, including employees who don't lead any project.
cursor.execute("""SELECT e.name, p.title
FROM employees e 
LEFT JOIN projects p on p.employee_id = e.id""")
print("QUERY 3")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")

# Query 4: Find employees who don't lead any project.
cursor.execute("""SELECT e.name, p.title
FROM employees e 
LEFT JOIN projects p on p.employee_id = e.id
WHERE p.title IS NULL
ORDER BY e.name""")

print("QUERY 4")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")


# Query 5: List all projects with the project lead's name AND their department name (requires joining 3 tables)
print("Query 5")
cursor.execute(
    """SELECT
    p.title,
    e.name,
    d.name
    FROM employees e
    JOIN projects p
        ON e.id = p.employee_id
    JOIN departments AS d
        ON d.id = e.department_id
    ORDER BY e.name
    """
)

for row in cursor.fetchall():
    print(row)


