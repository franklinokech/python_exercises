# import random from standard lib
import random
import math
import datetime as dt
import calendar as cal
import os
import platform


courses = ['Kis', 'History', 'Math', 'Physics', 'CompSci']

random_course = random.choices(courses)

print(random_course)

rads = math.radians(90)

print(rads)

print(platform.system())

print(dir(platform))

today = dt.date.today()
print(today)
print(cal.isleap(2020))

print(os.getcwd())

print(os.__file__)
