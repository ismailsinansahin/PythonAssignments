day = int(input("Please enter the day of date: "))
month = int(input("Please enter the month of date: "))
year = int(input("Please enter the year of date in two digits: "))
print(day,"/",month,"/",year)
if month * day == year :
    print("The date is magic")
else :
    print("The date is not magic")