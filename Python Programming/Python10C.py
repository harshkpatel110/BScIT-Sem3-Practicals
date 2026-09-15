import calendar
month=int(input("Enter month: "))
year=int(input("Enter year: "))
day=calendar.weekday(year,month,1)
print("Weekday:",calendar.day_name[day])