import pandas as pd
data = {
    "student": ["Alice", "Bob", "Charlie", "Diana", "Eve",
                 "Frank", "Grace", "Henry", "Iris", "Jack"],
    "course": ["Python", "Python", "SQL", "SQL", "Python",
               "SQL", "Python", "SQL", "Python", "SQL"],
    "score": [92, 78, 85, 91, 88, 72, 95, 68, 84, 90],
    "hours_studied": [20, 12, 18, 22, 15, 8, 25, 10, 16, 19],
    "passed": [True, True, True, True, True, False, True, False, True, True],
}
df = pd.DataFrame(data)
number_of_stu_by_course = df["course"].value_counts()
average = df.groupby("course")["score"].mean()

top_scorers = df.sort_values(by="score",ascending=False).head(3)
average_hours = df.groupby("passed")["hours_studied"].mean()
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score <= 60:
        return 'F'
df['grade'] = df['score'].apply(assign_grade)
grade_distribution = df.groupby(['course', 'grade']).size()
def display():
    print("*** Student Score Analysis ***")
    print(f"The data Frame \n\n {df}")
    print(f"Number of Students in each course: \n{number_of_stu_by_course}")
    print(f"Average score per course:\n {average}")
    print(f"Top three students:\n {top_scorers}")
    print(f"Average hours studied for students who passed vs did not passed:\n {average_hours}")
    print(f"Distribution of grade per course {grade_distribution}")
display()