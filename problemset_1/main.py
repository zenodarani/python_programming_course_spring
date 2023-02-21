# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years old.
from date import Date

# Assignment 0
def main():
    # Date before a person must have been born to be 21 or older.
    bornBefore = Date(10, 1, 1999)
    # Extract birth dates from the user and determine if 21 or older.
    date = promptAndExtractDate()
    while date is  not None:
        if date <= bornBefore:
            print("Is at least 21 years old: ", date)
        else:
            print("Sorry, not of age: ", date)
        date = promprAndExtractDate()

# Prompts for and extracts the Gregorian date components.
# Returns a Date object or None when the user has finshed entering dates
def promptAndExtractDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit)"))
    if month == 0:
        return None
    day = int(input("day: "))
    year = int(input("year: "))
    return Date(month, day, year)

# Call the main routine.
main()

