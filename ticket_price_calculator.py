"""
Name: Aniya Griffith
Date: 08/11/2024
Problem: Ticket Price Calculator program that calculates the ticket price for a movie theater based on age and time
"""

# Prompt user to enter their age and time of movie

age = int(input("Enter Age:"))
time = int(input("Enter Time in 24-hr format):"))

# Calculate ticket price based off age and time
if age < 12:
    price = 5
if 12 >= age >= 55:
    price = 7
elif age < 55:
    price = 10
if time < 1700:
    price -= 2

# Display final price of ticket for output

print("Your ticket price is: $",price)
