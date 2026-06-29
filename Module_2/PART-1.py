"""
Big O Time Complexity Exercises

This file contains several functions along with their time complexity
analysis.
"""

# ==================================================
# FUNCTION A
# ==================================================

def get_first(data):
    """Return the first element of a list."""
    return data[0]


# Time Complexity: O(1)
#
# Explanation:
# Accessing an element by its index takes constant time,
# regardless of the size of the list.


# ==================================================
# FUNCTION B
# ==================================================

def count_matches(data, target):
    """Count how many elements equal the target."""
    count = 0                  # O(1)

    for item in data:          # O(n)
        if item == target:     # O(1)
            count += 1         # O(1)

    return count               # O(1)


# Time Complexity: O(n)
#
# Explanation:
# The function examines every element in the list exactly once.


# ==================================================
# FUNCTION C
# ==================================================

def all_pairs(data):
    """Return every possible pair of elements."""
    pairs = []

    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))

    return pairs


# Time Complexity: O(n²)
#
# Explanation:
# The outer loop runs n times, and for each iteration,
# the inner loop also runs n times.
#
# Total operations:
# n × n = n²


# ==================================================
# FUNCTION D
# ==================================================

def mystery(n):
    """Count how many times n can be divided by 2."""
    count = 0

    while n > 1:
        n = n // 2
        count += 1

    return count


# Time Complexity: O(log n)
#
# Explanation:
# Each iteration cuts n in half, so the number of
# iterations grows logarithmically.


# ==================================================
# FUNCTION E
# ==================================================

def process(data):
    """Return the sum, sorted list, and first element."""
    total = sum(data)             # O(n)
    sorted_data = sorted(data)    # O(n log n)
    first = data[0]               # O(1)

    return total, sorted_data, first


# Time Complexity: O(n log n)
#
# Explanation:
# The function performs:
#   sum(data)      -> O(n)
#   sorted(data)   -> O(n log n)
#   data[0]        -> O(1)
#
# The dominant term is O(n log n), so the overall
# time complexity is O(n log n).