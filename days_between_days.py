# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def isLeapYear(year):
    if (year % 4 == 0):
        if not (year % 100 == 0):
            return True
    if (year % 400 == 0):
        return True
    return False
    
def daysInOneYear(year, month, day):
    days = 0
    for mo in range(month - 1):
        days += daysOfMonth[mo]
    days = days + day
    if isLeapYear(year) and month > 2:
        days += 1
    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = daysInOneYear(year2, month2, day2) - daysInOneYear(year1, month1, day1)
    for year in range(year1, year2):
        days += 365
        if isLeapYear(year):
            days += 1
    return days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", result
        else:
            print "Test case passed!", result

test()

print isLeapYear(2002), isLeapYear(2080)
print daysInOneYear(2012,3,1) - daysInOneYear(2012,1,1)

