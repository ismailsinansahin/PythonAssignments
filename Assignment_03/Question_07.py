cost=int(input("Price in cents: "))
quarters = (100-cost)//25
dimes = ((100-cost)%25)//10
nickles = (((100-cost)%25)%10)//5
pennies = (((100-cost)%25)%10)%5
print(f"Your change is {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies")
