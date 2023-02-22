# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years old.
from date import Date

def main():

    # Ask which assignment is to test
    assignment = asksAssignment()
    while assignment != 'e':
        assignment = int(assignment)
        # Assignment 0
        if assignment == 0:
            test0()
        # Assignment 1
        elif assignment == 1:
            test1()
        # Assignment 2
        elif assignment == 2:
            test2()
        assignment = asksAssignment()

# Tests functionalities of assignment 0
def test0():
    # Date before a person must have been born to be 21 or older.
    bornBefore = Date(21, 1, 2002)
    # Extract the date
    print("Enter a birth date.")
    date = promptAndExtractDate()
    while date is not None:
        # Check if at least 21 years old
        if date <= bornBefore:
            print("Is at least 21 years old: ", date)
        else:
            print("Sorry, not of age: ", date)
        print("Enter a birth date.")
        date = promptAndExtractDate()

# Tests functionalities of assignment 1
def test1():
    print("Enter a date.")
    date = promptAndExtractDate()
    print("Month name: ", date.monthName())
    print("Is leap year: ", date.isLeapYear())
    print("Enter another date.")
    date_2 = promptAndExtractDate()
    print("Number of days between the dates: ", date.numDays(date_2))
    days = int(input("Add a number of days to the second date: "))
    date_2.advanceBy(days)
    print(f"Result: {date_2.month()}.{date_2.day()}.{date_2.year()}")

# Tests functionalities of assignment 2
def test2():
    print('Insert a date: ')
    date = promptAndExtractDate()
    print('Day of the week: ', date.dayOfWeekName())
    print('Day of the year: ', date.dayOfYear())

# Prompts for and extracts the Gregorian date components.
# Returns a Date object or None when the user has finished entering dates
def promptAndExtractDate():
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    day = int(input("day: "))
    year = int(input("year: "))
    return Date(month, day, year)

# Asks which assignment to test
def asksAssignment():
    return input("\nAssignment to test ('e' to exit): ")

# Call the main routine.
main()

