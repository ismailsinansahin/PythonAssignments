mass = int(input("Please enter the number of mass: "))
weight = mass * 9.8
print("Object weight is" , weight , "newtons") 
if weight > 1000 :
    print("It is too heavy")
elif weight < 10 :
    print("It is too light")