#! /usr/bin/python3

from age import age_calc
import datetime

birthday = input("Wann sind Sie geboren? ")
date = input("Für welches Datum möchten Sie Ihr Alter wissen (dd.mm.yyyy)? ")
DefDate = datetime.datetime.strptime(date, "%d.%m.%Y")
age = age_calc(birthday, DefDate)
birth = datetime.datetime.strptime(birthday, "%d.%m.%Y")
print()
today = datetime.datetime.today()

if DefDate < today:
    print(f"Am {DefDate.day:02d}.{DefDate.month:02d}.{DefDate.year:04d} waren Sie {age} Jahre.")
else:
    print(f"Am {DefDate.day:02d}.{DefDate.month:02d}.{DefDate.year:04d} sind Sie {age} Jahre.")
