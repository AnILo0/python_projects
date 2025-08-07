"""
Name: Aniya Griffith
Date: 08/28/2024
Problem: Create a multiplication table program
"""


# Prompt user to enter a number or type 'exit' to end the program

def generate_multiplication_table(number):  # Define multiplication table
    print("f\nGenerating multiplication table for {number}:")
    for i in range(1, 12):  # Number of values used in multiplication table
        result = number * i
        print(f"{number} x {i} = {result}")  # Display output of results


def main():
    while True:
        user_input = input("Enter a number to generate multiplication table (or type 'exit' to end): ")
        if user_input.lower() == "exit":  # If user input is out of range exit
            print("Goodbye!")
            break
        if user_input.isdigit():  # If user input is in range start multiplication chart
            number = int(user_input)
            generate_multiplication_table(number)
        else:
            print("Please enter a valid number or 'exit' to quit.")


if __name__ == "__main__":
    main()
