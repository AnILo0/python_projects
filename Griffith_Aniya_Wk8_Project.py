"""
Name: Aniya Griffith
Date: 09/24/2024
Problem: Create Simple Library Program
"""


# Display the menu choices for the library
def display_menu():
    print("Library Tracking List:")
    print("1. Display available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit Program")


# Display list of available books
def available_books(library_list):
    print("Available books:")
    for book in library_list:
        print(f"- {book}")


# Borrow a book from the library
def borrow_book(library_list, borrowed_books):
    book = input("What book do you want to borrow? ")
    if book in library_list:
        library_list.remove(book)
        borrowed_books.append(book)
        print(f"You have borrowed '{book}'.")
    else:
        print(f"Sorry, '{book}' is not available.")


# Return a book to the library
def return_book(library_list, borrowed_books):
    book = input("What book do you want to return? ")
    if book in borrowed_books:
        borrowed_books.remove(book)
        library_list.append(book)
        print(f"'{book}' has been returned to the library.")
    else:
        print(f"You haven't borrowed '{book}'.")


def main():
    library_list = ['Comptia+ 701', 'Dorothy', 'Atomic Habits']
    borrowed_books_list = []

    while True:
        display_menu()
        choice = input('Enter choice (1, 2, 3, or 4): ')

        if choice == '1':
            available_books(library_list)
        elif choice == '2':
            borrow_book(library_list, borrowed_books_list)
        elif choice == '3':
            return_book(library_list, borrowed_books_list)
        elif choice == '4':
            print("Exit. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
