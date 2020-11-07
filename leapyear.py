# This is my program to find out if a year is a leap year
from datetime import datetime

year = input("Please give us a year(if current year then press enter): ")
today = datetime.today()
auto_year = today.year

if year == "" or year == "enter":
    if auto_year % 4 == 0:
        print("The current year is in fact a leap year!")
    else:
        print("Sorry mate, it ain't a leap year this year!")
else:
    if int(year) % 4 == 0:
        print("This is in fact a leap year!")
    else:
        print("Sorry mate, it ain't a leap year!")
