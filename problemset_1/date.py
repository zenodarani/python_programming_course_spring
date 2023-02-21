class Date:

    # Assignment 0
    # Creates an object of instance for the specified Gregorian date.
    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self.isValidGregorian(month, day, year), "Invalid Gregorian date."
        # calculate Julian Day
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + \
            1461 * (year + 4800 + tmp) // 4 + \
            367 * (month - 2 - tmp * 12) // 12 - \
            3 * ((year + 4900 + tmp) // 100) // 4

    # Extracts the appropriate Gregorian date component.
    def month(self):
        return (self._toGregorian())[0] #returning M from (M, d, y)

    def day(self):
        return (self._toGregorian())[1] #returning D from (m, D, y)

    def year(self):
        return (self._toGregorian())[2] # returning Y from (m, d, Y)

    # Returns day of the week as an int between 0 (Mon) and 6 (Sun).
    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 100 + year // 400) % 7

    # Logically compares the two dates.
    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay > otherDate._julianDay

    # Returns the Grgorian date as a tuple: (mont, day, year).
    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B-49) + year + A
        return month, day, year

    # Assignment 1
    # Returns the Gregorian month name of this date.
    def monthName(self):
        monthOfYear = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        # Gregorian months name have indexes in [0,11]
        month = self.month() - 1
        return monthOfYear[month]

    # Determines if this date falls in a leap year and returns the appropriate boolean value.
    def isLeapYear(self):
        year = self.year()
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return True
        return False

    # Returns the number of days as a positive integer between this date and the otherDate.
    def numDays(self, otherDate):
        return abs(self._julianDay - otherDate._julianDay)

    # Advances the date by the given number of days. The date is incremented if days is positive
    # and decremented if days are negative . The dare us capped to November 24, 4714 BC, if necessary.
    def advanceBy(self, days):
        self._julianDay += days
        if self._julianDay < 0:
            self._julianDay = 0

    # Return whether the three components of a date are valid (month, day, year)
    def isValidGregorian(self, month, day, year):
        if not (isinstance(month, int) and isinstance(day, int) and isinstance(year, int)):
            return False
        if day <= 0 or year <= -4713 or month < 1 or month > 12:
            return False
        # Check for month and corresponding days
        # 30 days months
        if month in [4, 6, 9, 11]:
            return day <= 30
        # 28 days month
        if month == 2:
            return day <= 28
        # 31 days months
        return day <= 31