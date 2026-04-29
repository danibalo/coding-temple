#!usr/env/python
#Telling user what to do
print("Enter three number after one each other")
# The try and except block for each number make sure the correct number is entered. If correct number is not given the program will exit.
try:
    num1 = int(input("Enter number 1: "))
except ValueError:
    print(f"That is not valid number use 0 instead")
    print("Exiting...")
    exit()
try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print(f"That is not valid number use 0 instead")
    print("Exiting...")
    exit()
try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print(f"That is not valid number use 0 instead")
    print("Exiting...")
    exit()
sum = num1 + num2 + num3
average = sum / 3
print(f"Your Numbers are: {num1}, {num2}, {num3}")
print(f"Sum: {sum}")
print(f"Average: {average:.2f}")

