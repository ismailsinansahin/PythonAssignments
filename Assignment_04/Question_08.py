packages = int(input("Please enter the number of packages you purchased: "))
if 10 <= packages <=19 :
    discount = (packages * 99) * 0.20
if 20 <= packages <= 49 :
    discount = (packages * 99) * 0.30
if 50 <= packages <= 99 :
    discount = (packages * 99) * 0.40
if packages >= 100 :
    discount = (packages * 99) * 0.50
else :
    discount = 0
print("Your discount is: ", discount)
print("Your total amount is:", (packages * 99) - discount)