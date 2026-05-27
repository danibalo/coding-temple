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
        with open (filepath, 'r', newline='') as file:
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
    valid_grades = []
    for grade in grades:
        try:
            valid_grades.append(float(grade))

        except ValueError:
            continue
    if len(valid_grades) == 0:
        return None
    average = sum(valid_grades) / len(valid_grades)
    return round(average, 1)
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
    if average is None:
        return "N/A"
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
    student_summaries = []
    all_averages = []
    grade_distribution = {
        "A":0,
        "B":0,
        "C":0,
        "D":0,
        "F":0,
        "N/A":0
        }

    for student in students:
        grade = [student['math'], student['science'], student['english'],student['history']]
        average = calculate_average(grade)
        grade_in_letter = get_letter_grade(average)
        student_summary = {
                    "name": student["student_name"],
                    "average": average,
                    "grade": grade_in_letter
                    }
        student_summaries.append(student_summary)
        grade_distribution[grade_in_letter] +=1
        if average is not None:
            all_averages.append(average)




    return {
            "total_students": total_students,
            "class_average": round(sum(all_averages) / len(all_averages),1) if all_averages else None,
            "highest_average": max(all_averages),
            "lowest_average": min(all_averages),
            "grade_distribution": grade_distribution,
            "students": student_summaries
            }

def write_report(report:dict, filepath:str) -> None:
    """
    Write the summary report to a text file.
    Format example:
    =========================================
    STUDENT GRADE REPORT
    =========================================
    Total students: 15
    Class average: 81.3
    Highest average: 95.0
    Lowest average: 55.0

    Grade Distribution:
    A: 5
    B: 4
    ....

    Individual Results:
    Alice Johnson Avg: 91.5 Grade: A
    ......
    Args:
     report: The dict returned by generate_report().
     filepath: Path to write the report file.

    
    
    """
    #Todo: Open the file in write mode("w").
    #      Write each section with f-strings.
    #      use f.write() or print(...,file=f)
    with open("grade_report.txt", "w", newline="") as file:
        file.write(f"{'='*45}")
        file.write(f"\nSTUEDENT GRADE REPORT")
        file.write(f"\n{'='*45}")
        file.write(f"\nTotal students: {report['total_students']}")
        file.write(f"\nClass average: {report['class_average']}")
        file.write(f"\nHighest averagge: {report['highest_average']}")
        file.write(f"\nLowest average: {report['lowest_average']}\n")
        file.write(f"\nGrade Distribution\n")
        for grade,count in report['grade_distribution'].items():
            file.write(f"{grade}:{count}\n")
        file.write(f"\nIndividual Results:\n")
        for student in report['students']:
            file.write(f"{student['name']} Avg: {student['average']} Grade: {student['grade']}\n")
        



def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")
    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students: {report['total_students']}")
    print(f"Class average: {report['class_average']}")
    print(f"Highest average: {report['highest_average']}")
    print(f"Lowest average: {report['lowest_average']}")
    print("\nGrade Distribution:")
    for grade, count in sorted(report['grade_distribution'].items()):
        print(f" {grade}: {count}")
    print(f"\nTop students:")
    sorted_students = sorted(
            [s for s in report["students"] if s["average"] is not None],
            key=lambda s: s["average"],
             reverse=True)
    for s in sorted_students[:5]:
        print(f" {s['name']:<20} {s['average']:.1f} ({s['grade']})")
    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")

if __name__ == "__main__":
    main()
