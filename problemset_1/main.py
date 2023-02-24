# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years old.
from date import Date
from copy import copy

def main():
    date1 = inputDate('Insert a date (month.day.year): ')
    date2 = inputDate('Insert a second date (month.day.year): ')
    print('First date: ', date1.asGregorian())
    print('Second date: ', date2.asGregorian())

    # Assignment 1
    print('----Assignment 1----')
    print(f'Month of {date1.asGregorian()}: {date1.monthName()}')
    print(f'Is year of {date1.asGregorian()} a leap year? {date1.isLeapYear()}')
    print(f'Days between {date1.asGregorian()} and {date2.asGregorian()}: {date1.numDays(date2)}')
    days = int(input(f'Insert a number of days to add at {date2.asGregorian()}: '))
    oldDate2 = copy(date2)
    date2.advanceBy(days)
    print(f'{oldDate2.asGregorian()} + {days} = {date2.asGregorian()}')

    # Assignment 2



# Ask for a date and returns it.
def inputDate(msg):
    strDate = input(msg)
    month, day, year = strDate.split('.')
    month = int(month)
    day = int(day)
    year = int(year)
    return Date(month, day, year)

# Call the main routine.
main()

