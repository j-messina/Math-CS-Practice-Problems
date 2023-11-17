# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months_num_days = {
    "January":31,
    "February":28,
    "March":31,
    "April":30,
    "May":31,
    "June":30,
    "July":31,
    "August":31,
    "September":30,
    "October":31,
    "November":30,
    "December":31
}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

def newYear_MonthDays(year):
    return [31, 28+isLeapYear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_year = 1901
end_year = 2000

this_years_monthdays = newYear_MonthDays(start_year)
current_year = start_year
current_weekday = 0 # Monday
current_month = 0
current_monthday = 1 # the 1st of the month

sundays_count = 0


while current_year <= 2000:
    # print("Today is {}, on day {} of month {} in the year {}".format(weekdays[current_weekday], current_monthday,                                                           months[current_month], current_year))
    if current_weekday == 6:
        if current_monthday == 2:
            sundays_count += 1
        current_weekday = 0
    else:
        current_weekday += 1
    current_monthday += 1
    if current_monthday > this_years_monthdays[current_month]:
        current_month += 1
        current_monthday = 1
        if current_month >= len(months):
            current_month = 0
            current_year += 1
            this_years_monthdays = newYear_MonthDays(current_year)

print('Total number of Sundays from January 1st 1900 to December 31st 2000: ', sundays_count)


