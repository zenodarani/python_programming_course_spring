# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years old.
from date import Date

def main():
    # Assignment 0
    # Date before a person must have been born to be 21 or older.
    bornBefore = Date(10, 1, 1999)
    # Extract the date
    date = promptAndExtractDate()
    while date is not None:
        # Check if at least 21 years old
        if date <= bornBefore:
            print("Is at least 21 years old: ", date)
        else:
            print("Sorry, not of age: ", date)

        date = promptAndExtractDate()

# Prompts for and extracts the Gregorian date components.
# Returns a Date object or None when the user has finished entering dates
def promptAndExtractDate():
    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    day = int(input("day: "))
    year = int(input("year: "))
    return Date(month, day, year)

# Call the main routine.
main()

