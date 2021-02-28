import calendar

# Use HTMLCalendar for HTML view and TextCalendar for text format
'''tc= calendar.HTMLCalendar(firstweekday=0)
print(tc.formatmonth(2016, 5))'''
#initialis with first day as sunday for the month
c = calendar.TextCalendar(calendar.SUNDAY)
#make calendar for 2020 apr
cal_format = c.formatmonth(2020,4)

print(cal_format)

# echo full calendar
cal_year = c.formatyear(2020)



print(cal_week)
# loop over the day of month
# 0 are days of other months

for i in c.itermonthdays(2020,4):
    print(i)

# looping in the month names in cal
for days in calendar.month_name:
    print(days)

# looping in the day name in year
for data in calendar.day_name:
    print(data)
