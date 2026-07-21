def is_balanced(text):
    """Return True if brackets in text are properly matched.
    Handles (), {}, []
    """
    stack = []
    # Matching Pairs
    pairs = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    for char in text:
        #Opening bracket
        if char in "({[":
            stack.append(char)
        #closing bracket
        elif char in ")}]":
            if not stack:
                return False
        #Remove the last opening brackets
            top = stack.pop()
            if top != pairs[char]:
                return False
    return len(stack) == 0
# Tests:
print(is_balanced("()"))           # True
print(is_balanced("({[]})"))       # True
print(is_balanced("(]"))           # False
print(is_balanced("([)]"))         # False
print(is_balanced("hello (world)")) # True