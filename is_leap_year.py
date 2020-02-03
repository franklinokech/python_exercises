# Number of days per mont
month_days = [0, 31, 28, 31,	30, 31,	30, 31,	31, 30, 31, 30, 31]

# Leap year occures every 4 years, except for years that are divisable by
# # 100 and not divisable by 400.


def is_leap(year):
    """Return True for leap year, False for non-leap years. """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return the number of days in a month"""

    if not month >= 1 and month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2010, 2))
