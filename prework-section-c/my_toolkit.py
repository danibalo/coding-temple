#!/usr/env/python
def calculate_average(numbers):
    """
    Returns the average of a list of numbers

    """
    sum_scores = 0
    if numbers:
        for num in numbers:
            sum_scores += num
        return sum_scores / len(numbers)
    else:
        return 0
def find_max_and_min(numbers):
    """ Returns the max_value and min_value of a list of numbers as tuple form"""
    max_value = numbers[0]
    min_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return (max_value, min_value)
def count_occurrences(items, target):
    """ Return how many times the target appeared in listed number"""
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
def is_palindrome(text):
    new_text = ""
    for ch in text.lower():
        if ch == " ":
            continue
        new_text += ch
    return new_text == new_text[::-1]
def create_report(title, scores):
    return f"------{title}------\nAverage: {calculate_average(scores):.2f}\nMaximum, Minimum values: {find_max_and_min(scores)}"













if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    

