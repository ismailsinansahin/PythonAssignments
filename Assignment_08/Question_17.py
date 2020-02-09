def getThunderBlazz(availability, gift, ing1, ing2, ing3):
    if availability or gift or ((ing1==1 and ing2==2 and ing3==3) or (ing1==3 and ing2==1 and ing3==2)):          
        return True
    else:
        return False  
    
availability = int(input("Is there any drink available / '1' for True / '0' for False :")) 
gift = int(input("Is there any coupon available / '1' for True / '0' for False :"))     
ing1 = int(input("Enter the ingredient-1 amount : "))
ing2 = int(input("Enter the ingredient-2 amount : "))
ing3 = int(input("Enter the ingredient-3 amount : ")) 

print(getThunderBlazz(availability, gift, ing1, ing2, ing3))


# Is there any drink available / '1' for True / '0' for False :0
# Is there any coupon available / '1' for True / '0' for False :1
# Enter the ingredient-1 amount : 1
# Enter the ingredient-2 amount : 2
# Enter the ingredient-3 amount : 4
# True

# Is there any drink available / '1' for True / '0' for False :0
# Is there any coupon available / '1' for True / '0' for False :0
# Enter the ingredient-1 amount : 1
# Enter the ingredient-2 amount : 2
# Enter the ingredient-3 amount : 4
# False

# Is there any drink available / '1' for True / '0' for False :0
# Is there any coupon available / '1' for True / '0' for False :0
# Enter the ingredient-1 amount : 1
# Enter the ingredient-2 amount : 2
# Enter the ingredient-3 amount : 3
# True

# Is there any drink available / '1' for True / '0' for False :0
# Is there any coupon available / '1' for True / '0' for False :0
# Enter the ingredient-1 amount : 3
# Enter the ingredient-2 amount : 1
# Enter the ingredient-3 amount : 2
# True

