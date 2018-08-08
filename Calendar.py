import calendar

year = int (input("Please Enter the year Number: "))
month = int (input("Please Enter the month Number: "))

print ("\n ----------")
print (calendar.month(year, month))

c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2018, 1) # 2018 means the year and the 1 means the month
print (str)
