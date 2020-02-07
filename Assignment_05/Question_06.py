year = int(input("Please enter the model year of your car: "))
if 1995<=year<=1998 or 2001<=year<=2002 or 2004<=year<=2006 or 2015<=year<=2017:
    print("Your vehicle needs to be recalled!")
else:
    print("Your vehicle is fine, enjoy!")