""" The answers are stated under each function"""
# Function A
def reverse_string(s):
    return s[::-1]
# Space complexity O(n)
# Reason: Cause string in python are immutable slicing operation does not affect the original string, it creates new string containing all n characters in reverse order.




# Function B
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts
#Space Complexity O(n)
#Reason: The dictionary counts can grow to store one entry for every unique character in the input, which in the worst case is proportiional to input size.

# Function C
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# SPACE COMPLEXITY O(n2)
#Reason: The function allocates and returns n * n matrix, so it provides n square of 2 elements



# Function D
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)
# SPACE COMPLEXITY O(1)
#REASON: The function only uses two extra variables (total and num), regardles of how many numbers are in the input.

