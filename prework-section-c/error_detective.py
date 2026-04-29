#!/usr/enc/python
###  Snippet1 ######

print("The answer is: " + 42)

#my prediction: Type error, string and int data types can be concatenated or added as in math
#The Actual error:
r"""Traceback (most recent call last):
  File "C:\Users\daniy\OneDrive\Desktop\Coding temple\coding-temple\prework-section-c\error_detective.py", line 3, in <module>
    print("The answer is: " + 42)
          ~~~~~~~~~~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str """

### Snippet2 ###

favorite = input("Favorite nember: ")
result = favorite + 10
print(result)
#my prediction: TYPE ERROR, string and int data type can't be concanated 
#The actual error:
r"""
$ python  error_detective.py
Favorite nember: 5
Traceback (most recent call last):
  File "C:\Users\daniy\OneDrive\Desktop\Coding temple\coding-temple\prework-section-c\error_detective.py", line 16, in <module>
    result = favorite + 10
             ~~~~~~~~~^~~~
TypeError: can only concatenate str (not "int") to str
"""
### Snippet 3 ###

print("Hello World)

#My prediction: SYNTAX ERROR, Stirings in print function has to be in qoute

#ACTUAL ERROR :
r""" $ python  error_detective.py
  File "C:\Users\daniy\OneDrive\Desktop\Coding temple\coding-temple\prework-section-c\error_detective.py", line 30
    print("Hello World)
          ^
SyntaxError: unterminated string literal (detected at line 30) """
### Snippet 4 ###

age = int("twenty five")

#My prediction: VALUE ERROR, as we cannot convert string characters to int

#ACTUAL ERROR
r"""$ python  error_detective.py
Traceback (most recent call last):
  File "C:\Users\daniy\OneDrive\Desktop\Coding temple\coding-temple\prework-section-c\error_detective.py", line 40, in <module>
    age = int("twenty five")
ValueError: invalid literal for int() with base 10: 'twenty five'
"""
### Snippet 5 ###

print(username)

#my prediction: NAME ERROR, there is no variable named as username in the code
#ACTUAL ERROR:
r""" $ python  error_detective.py
Traceback (most recent call last):
  File "C:\Users\daniy\OneDrive\Desktop\Coding temple\coding-temple\prework-section-c\error_detective.py", line 51, in <module>
    print(username)
          ^^^^^^^^
NameError: name 'username' is not defined
"""
