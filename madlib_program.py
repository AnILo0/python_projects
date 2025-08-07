"""
Name: Aniya Griffith
Date: 09/20/2024
Problem: Create MadLib Program
"""


def military_madlib(name, verb1, verb2, noun1, noun2, adjective1, adjective2, integer1, integer2):
    madlib_story = f"""
        {name} wakes up at {integer1} a.m., grabs their {noun1}, and heads out.The
        day starts with intense {verb1}, making everyone feel {adjective1}. By {integer2} p.m.,
        it's time to {verb2} the base,ensuring everything is {adjective2}. After a long day, {name}
        kicks back with their {noun2}, ready for whatever tomorrow brings.
        """
    return madlib_story


def main():
    # Input data for Madlib
    name = input("What is your name? ").capitalize()
    verb1 = input("Enter a plural verb: ")
    verb2 = input("Enter a singular verb: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a second noun: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter a second adjective: ")
    integer1 = input("Enter an integer: ")
    integer2 = input("Enter a second integer: ")

    # Generate story
    madlib_story = military_madlib(name, verb1, verb2, noun1, noun2, adjective1, adjective2, integer1, integer2)

    # Display and print Mad Lib story output
    print(madlib_story)


if __name__ == "__main__":
    main()

