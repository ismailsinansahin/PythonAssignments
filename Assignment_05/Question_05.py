age = int(input("Please enter the age: "))
print("Age =", age)
if age<=2:
    print(age, ", toddler")
elif 3<=age<=5:
    print(age, ", early childhood")
elif 6<=age<=7:
    print(age, ", young reader")
elif 8<=age<=10:
    print(age, ", elemantary")
elif 11<=age<=12:
    print(age, ", middle")
elif age==13:
    print(age, ", impossible")
elif 14<=age<=16:
    print(age, ", high school")
elif 17<=age<=18:
    print(age, ", scholar")
elif age>18:
    print(age, ", ineligible")
