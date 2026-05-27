"""
Project: Student Grade Tracker
Pre-Work Section C - Python Fundamentals
Estimated time: 45-60 minutes

Objective: Build a data processing script that reads student grades from a CSV, calculate averages, assigns letter grades, and writes a summary report.

"""
import csv
# ==================================================
# FUNCTION 1: Load data from CSV
# ==================================================

def load_students(filepath: str) -> list[dict]:

    """
    Read student data from a CSV file.
    Each row become a dictionary. The CSV has columns:
    student_name, math, science, english, history

    Some cells may be empty strings (missing grades) - that's expected.

    Args:
        filepath: Path to the CSV file.
    Returns:
        A list of dicts, one per student.
        Example: [{"student_name": "Alice", "math":"92", "science":...},...}]

    Raises:
        FileNotFoundError: if the CSV file doesn't exist.

    """
    try:
        with open (filepath, 'r') as file:
            students = []
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        return students
    except FileNotFoundError:
        return []


# ======================================================
# FUNCTION 2: Calculate average, handling missing values
# =======================================================
def calculate_average(grades: list) -> float | None:
    """
    Calculate the average of a list of grade values.
    Grade values may be stirngs (from CSV ), empty strings, or numbers.
    Ignore any value that can't be converted to a float.

    Args:
        grades: A list of values (e.g., ["92", "88", "", "79"]).
    Returns:
        The average as a float, rounded to 1 decimal place.
        Returns None if there are no valid grades.
    """
    grades = []
    for grade in grades:
        if float(grade):
            grades.append(float(grade))
        else:
            continue
    try:
        average = sum(grades) / len(grades)
        return round(average, 1)
    except ZeroDivisionError:
        return None
# ==============================================
# Function 3: Assign letter grade
#===============================================
def get_letter_grade(average: float | None) -> str:
    """
    Convert a numeric average to a letter grade.
    Scale:
    90+ → "A"
    80-89 → "B"
    70-79 → "C"
    60-69 → "D"
    < 60 → "F"
    None → "N/A" (no grades available)
    Args:
    average: The numeric average, or None.
    Returns:
    The letter grade as a string.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average < 60:
        return "F"
    else:
        return "N/A (no grades available)"
# ==============================================
# FUNCTION 4: Generate summary report
#===============================================
def generate_report(students: list[dict]) -> dict:
    """
    Generate a class summary report.
    Args:
    students: The list of student dicts from load_students()
    Returns:
    A dict with these keys:
        "total_students": int - how many students
        "class_average": float - average of all valid averages
        "highest_average": float - the best average
        "lowest_average": float - the lowest average
        "grade_distribution": dict - {"A": 3, "B": 5,....}
        "students": list of dicts, each with:
                     name, average, grade
        """
        #TODO: For each student:
        # 1. Extract grades (math, science, english, history values)
        # 2. Call calculate_average()
        # 3. Call get_letter_grade()
        # 4. Build the student summary dict
        # Then compute class-level stats from all the averages.
    total_students = len(students)
    for student in students:
        grades = [student["math"], student["science"], student["english"], student["history"]]
        average = calculate_average(grades)
        grade = get_letter_grade(average)
        student_summary = {"total_students": total_students, "average": average, "grade": grade}
    return {student_summary}




def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")
    print("Generating report...")
    report = generate_report(students)
    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")


if __name__ == "__main__":
    main()
