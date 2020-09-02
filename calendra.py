import calendar

import time
print(calendar.weekheader(4))
print("")

print(calendar.firstweekday())
print("")
print(calendar.month(2050, 3, ))
print(calendar.monthcalendar(2020, 3))
print(calendar.calendar(2050))
print(calendar.calendar(2200))
for x in range(12):
	print("Month is " + calendar.month(2050,x+1))
	print(calendar.monthcalendar(2050,x+1))

day_of_week = calendar.weekday(2020, 5,24)
print(day_of_week)

is_it_leap = calendar.isleap(2016)
print(is_it_leap)

how_many_leap_days = calendar.leapdays(2000,3000)
print(how_many_leap_days)

print(time.localtime())