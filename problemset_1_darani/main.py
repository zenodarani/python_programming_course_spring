from date import Date
from copy import deepcopy

# Tests all the functionalities of the class Date
def main():
    date1 = inputDate('Insert a date (month.day.year or "enter" for today): ')
    date2 = inputDate('Insert a second date (month.day.year or "enter" for today): ')
    print('First date: ', date1.asGregorian())
    print('Second date: ', date2.asGregorian())

    # Assignment 1
    print('\n----Assignment 1----')
    print(f'Month of {date1.asGregorian()}: {date1.monthName()}')
    print(f'Is year of {date1.asGregorian()} a leap year? {date1.isLeapYear()}')
    print(f'Days between {date1.asGregorian()} and {date2.asGregorian()}: {date1.numDays(date2)}')
    days = int(input(f'Insert a number of days to add at {date2.asGregorian()}: '))
    oldDate2 = deepcopy(date2)
    date2.advanceBy(days)
    print(f'{oldDate2.asGregorian()} + {days} = {date2.asGregorian()}')

    # Assignment 2
    print('\n----Assignment 2----')
    print(f'Day of the week of {date1.asGregorian()}: {date1.dayOfWeekName()}')
    print(f'Day of the year of {date1.asGregorian()}: {date1.dayOfYear()}')
    print(f'Is {date1.asGregorian()} a weekday? {date1.isWeekday()}')
    print(f'Is {date1.asGregorian()} an equinox? {date1.isEquinox()}')
    print(f'Is {date1.asGregorian()} a solstice? {date1.isSolstice()}')

    # Assignment 3
    print('\n----Assignment 3----\n')
    printCalendar(date1)

    # Assignment 4
    print('\n----Assignment 4----')
    params = {}
    month = input('Insert a month (press "enter" to use current month): ')
    if month != '':
        params['month'] = int(month)
    day = input('Insert a day (press "enter" to use current day): ')
    if day != '':
        params['day'] = int(day)
    year = input('Insert a year (press "enter" to use current year): ')
    if year != '':
        params['year'] = int(year)
    date3 = Date(**params)
    print(date3.asGregorian())


# Ask for a date and returns it.
def inputDate(msg):
    strDate = input(msg)
    if strDate == '':
        return Date()
    month, day, year = strDate.split('.')
    month = int(month)
    day = int(day)
    year = int(year)
    return Date(month, day, year)


# Given a date it prints the month calendar of that date
def printCalendar(date):
    # print month and year centered
    title = f'{date.monthName()} {date.year()}'
    numSpaces = (26 - len(title)) // 2
    print(f"{' '*numSpaces}{title}\n")
    print('Su  Mo  Tu  We  Th  Fr  Sa')
    currentDay = Date(date.month(), 1, date.year())
    # prints initial empty spaces
    dayOfWeekOrder = [6, 0, 1, 2, 3, 4, 5]
    i = 0
    while dayOfWeekOrder[i] != currentDay.dayOfWeek():
        print('    ', end='')
        i += 1
    # prints the days
    while currentDay.month() == date.month():
        print(currentDay.day(), end='')
        if currentDay.day() < 10:
            print(' ', end='')
        if currentDay.dayOfWeek() == dayOfWeekOrder[-1]:
            # new line
            print()
        else:
            print('  ', end='')
        currentDay.advanceBy(1)
    print()


# Call the main routine.
main()

