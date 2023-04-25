import sys

try:
    x = int(input("enter x "))
    y = int(input("enter y "))
except ValueError:
    print("please enter x ")

try:
    result = x / y
except ZeroDivisionError:
    print("Error:can not divide by zero")
    sys.exit(1)

print(result)
