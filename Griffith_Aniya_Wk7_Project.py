"""
Name: Aniya Griffith
Date: 09/21/2024
Problem: Create Movie Recommendation List Program
"""


def display_menu():
    print('Movie Recommendations List')
    print('1. Add movie to list:')
    print('2. Display movie recommendations:')
    print('3. Exit')


def add_movie(movie_list):
    movie = input('Enter a movie name:')
    print('{movie} added to list')
    movie_list.append(movie)


def display_recommendation(movie_list):
    if not movie_list:
        print('No recommendations')
    else:
        print('Movie recommendations:')
        for movie in movie_list:
            print(movie)


def main():
    movie_list = []
    while True:
        display_menu()
        choice = input('Enter choice (1, 2, or 3):')

        if choice == '1':
            add_movie(movie_list)
        elif choice == '2':
            display_recommendation(movie_list)
        elif choice == '3':
            print('Exit. Goodbye')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
