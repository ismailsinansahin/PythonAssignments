weight = int(input("Please enter the weight of your package: "))
miles = int(input("Please enter the miles your package will be sent: "))

if weight <= 2 :
    charge = (miles // 500) * 1.10
if 2 < weight <= 6 :
    charge = (miles // 500) * 2.20
if 6 < weight <= 10 :
    charge = (miles // 500) * 3.70
if weight > 10 :
    charge = (miles // 500) * 3.80
    
print("Your charge is:", charge)