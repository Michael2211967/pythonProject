#! /usr/bin/python3

from datetime import date, datetime

def age_calc(birthday, date=date.today()):
    today = datetime.combine(date, datetime.min.time())
    birth = datetime.strptime(birthday, "%d.%m.%Y")
    age = today.year - birth.year

    if today.month < birth.month or (today.month == birth.month and today.day < birth.day):
        age -= 1

    return age

if __name__ == "__main__":
    birthday = input("Wann sind Sie geboren? ")
    date_1 = date(2000,11,22)
    age = age_calc(birthday)
    today = date.today().strftime("%d.%m.")
    #today = date.strftime("%d.%m.")
    #print(today)
    print()
    print(f"Sie sind aktuell {age} Jahre alt.")
    if today == birthday[0:6]:
        print(f"Herzliche Grüsse zum {age}. Geburtstag.")
    print()
    year = int(birthday[6:10])
    day = int(birthday[0:2])
    month = int(birthday[3:5])
    for i in range(year + 1, year + 81):
        date_2 = date(i,month,day)
        age = age_calc(birthday, date_2)
        print(f"Geburtstag: {date_2:%d.%m.%Y}: {age:>2} Jahre")
