"""
Name: Aniya Griffith
Date: 08/30/2024
Problem: create a Pizza Ordering program
"""


# Function to display pizza menu and get user choice
def get_pizza_size():
    print("Menu:")
    print("1. Small cheese pizza - $8.00")
    print("2. Medium cheese pizza - $10.99")
    print("3. Large cheese pizza - $11.99")

    while True:
        try:
            size_choice = int(input("Enter the number for the size of pizza you want (1/2/3): "))
            if size_choice == 1:
                return "Small", 8.00
            elif size_choice == 2:
                return "Medium", 10.99
            elif size_choice == 3:
                return "Large", 11.99
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to get the number of pizzas the user wants
def get_quantity():
    while True:
        try:
            quantity = int(input("How many pizzas would you like to order? "))
            if quantity > 0:
                return quantity
            else:
                print("Please enter a valid quantity.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to get topping choices from the user
def get_toppings():
    toppings = {"pepperoni": 0, "sausage": 0, "olives": 0}
    print("Toppings: 1 for Yes, 0 for No ($1 extra for each)")

    for topping in toppings:
        while True:
            try:
                choice = int(input(f"Do you want {topping}? (1 for Yes, 0 for No): "))
                if choice in [0, 1]:
                    toppings[topping] = choice
                    break
                else:
                    print("Invalid choice, please enter 1 or 0.")
            except ValueError:
                print("Invalid input. Please enter 1 or 0.")

    return toppings


# Function to calculate the total price
def calculate_total(price, quantity, toppings):
    total_toppings = sum(toppings.values())
    total_price = (price * quantity) + total_toppings * quantity  # $1 per topping per pizza
    return total_price


# Function to display the order confirmation
def display_order(size, quantity, toppings, total_price):
    print("\n--- Order Confirmation ---")
    print(f"Pizza size: {size}")
    print(f"Quantity: {quantity}")
    print(
        f"Toppings: {', '.join([key for key, value in toppings.items() if value == 1]) if sum(toppings.values()) > 0 else 'No toppings'}")
    print(f"Total price: ${total_price:.2f}")
    print("Thank you for your order!")


# Main function to handle the pizza ordering process
def pizza_order_program():
    size, price = get_pizza_size()  # Get pizza size and base price
    quantity = get_quantity()  # Get quantity of pizzas
    toppings = get_toppings()  # Get toppings choices
    total_price = calculate_total(price, quantity, toppings)  # Calculate total price
    display_order(size, quantity, toppings, total_price)  # Display order receipt


# Call the main function to start the program
if __name__ == "__main__":
    pizza_order_program()
