"""
Name: Aniya Griffith
Date: 08/10/2024
Problem: create a calculator program that uses addition, subtraction, multiplication, and division
"""

# Prompt user to use 4 different values for input

n1 = float(input("enter first value"))
n2 = float(input("enter second value"))
n3 = float(input("enter third value"))
n4 = float(input("enter fourth value"))


# Use arithmetic operations for processing

def addition(n1, n3):
    result = n1 + n3
    return result


def subtraction(n2, n3):
    result = n2 - n3
    return result


def multiplication(n1, n4):
    result = n1 * n4
    return result


def division(n3, n1):
    result = n1 / n3
    return result


# Display name of operation and results for each arithmetic operations for output

print("the result of addition is:", addition(n1, n3))
print("the result of subtraction is:", subtraction(n2, n3))
print("the result of multiplication is:", multiplication(n1, n4))
print("the result of division is:", division(n3, n1))
