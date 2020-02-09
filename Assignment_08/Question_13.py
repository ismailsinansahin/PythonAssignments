def waterTax(unit):
    if unit<=50:
        bill = unit*0.60
    elif 51<=unit<=100:
        bill = unit*0.90
    elif 101<=unit<=150:
        bill = unit*0.90 + 50
    elif unit>150:
        bill = unit*0.90 + 100
        
    return bill
  
unit = int(input("Please enter howmany units of water did you use? : "))      
print("Your bill is = ", waterTax(unit))


# Please enter howmany units of water did you use? : 50
# Your bill is =  30.0

# Please enter howmany units of water did you use? : 80
# Your bill is =  72.0

# Please enter howmany units of water did you use? : 120
# Your bill is =  158.0

# Please enter howmany units of water did you use? : 200
# Your bill is =  280.0