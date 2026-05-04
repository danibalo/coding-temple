#scores is a list of student scores. The program calculates the highest, lowest, average, and pass/fail counts, and displays the results. It also allows the user to add more scores and updates the analysis accordingly.
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
# Function to calculate the highest score
def highest():
    max = scores [0]
    for score in scores:
        if score > max:
            max = score
    return max
# Function to calculate the lowest score
def lowest():
    min = scores[0]
    for score in scores:
        if score < min:
            min = score
    return min
#function to calculate number of passing and failing students
def pass_fail():
    pass_count = 0
    fail_count = 0
    for score in scores:
        if score > 60:
            pass_count += 1
    for score in scores:
        if score < 60:
            fail_count += 1
    print(f"Passing: {pass_count} ({pass_count/len(scores) * 100:.2f}%)")
    print(f"Failing: {fail_count} ({fail_count/len(scores) * 100:.2f}%)")
#a function to calculate the average score
def average():
    sum = 0
    for score in scores:
         sum += score
    return sum / len(scores)
# a function to display the grade analysis results, including total scores, average, highest, lowest, and pass/fail counts.
def gradeAnalyzer_display():
    print(f"{'='*3} Grade Analyzer {'='*3}")
    print(f"Total Scores: {len(scores)}")
    print(f"Average: {average():.2f}")
    print(f"Highest: {highest()}")
    print(f"Lowest: {lowest()}")
    pass_fail()
gradeAnalyzer_display()
# a function to calculate the grade distribution based on the scores, counting how many students received each letter grade (A, B, C, D, F) and displaying the results.
def grade_calculator():
    print("\nGrade Distribution: ")
    grade = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for score in scores:
        if score >= 90:
            grade['A'] += 1
        elif score > 80:
            grade['B'] += 1
        elif score >= 70:
            grade['C'] +=1 
        elif score >= 60:
            grade['D'] += 1
        else:
            grade['F'] += 1
    for grade, count in grade.items():
        print(f"{grade}: {count} students")
grade_calculator()
# a function to allow the user to add more scores to the list, and then re-calculate and display the updated grade analysis results.
def add_score():
    print(f"--- ADD MORE SCORES --")
    try:
        score = input("Enter a score or ('done') to finish): ")
        while score != 'done':
            scores.append(int(score))
            score = input("Enter a score or ('done') to finish): ")
        gradeAnalyzer_display()
        grade_calculator()
    except ValueError:
        print("Invalid input. Please enter a valid score.")
    
add_score()



