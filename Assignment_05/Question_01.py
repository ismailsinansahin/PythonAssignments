numberOfBedrooms = input("Please enter the number of bedrooms you are looking for: ")
if numberOfBedrooms == "1":
    startingPrice = 1100
    print("Starting Price", startingPrice)
elif numberOfBedrooms == "2":
    startingPrice = 1850
    print("Starting Price", startingPrice)
elif numberOfBedrooms == "3":
    startingPrice = 2550
    print("Starting Price", startingPrice)
else:
    print("No such bedrooms available")


