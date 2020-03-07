"""
Write a program that will calculate laptop price based on the components.

First, ask user for screen size.
 If screen size equals to 13.3, add $200 to the laptop price.
 If screen size equals to 15.0 - add $300 to the laptop price. 
 If screen size equals to 17.3 - add $400 to the laptop price.

Then ask the user for CPU type. 
If CPU type equals to i3, add $150 to the laptop price. 
If CPU type equals to i5, add $250 to the laptop price. 
If CPU type equals to i7, add $350 to the laptop price.

Then ask the user for RAM size. Add $50 for every 4GB of ram to the laptop price.

Then, ask the user for the storage type. There are 2 options: SSD and HDD. 
If it's HDD - add $50 to the laptop price for every 500gb. 
If it's SSD - add $100 to the laptop price for every 500GB.

Then ask the user for screen resolution. There are 2 options: FULLHD and 4K. 
Add $100 if it's FULLHD screen and $200 if it's 4K screen.

Sample Output:

Display message: Select screen size:
input: 13.3
Display message: Select CPU type:
input: i7
Display message: Select RAM size:
input: 8
Display message: Select storage type:
input: SSD
Display message: Enter memory size:
input: 1000
Display message: Enter screen resolution:
input: 4K
Display message: Laptop price is: $1050.0
Example #2

Display message: Select screen size:
input: 13.3
Display message: Select CPU type:
input: i3
Display message: Select RAM size:
input: 4
Display message: Select storage type:
input: HDD
Display message: Enter memory size:
input: 500
Display message: Enter screen resolution:
input: FULLHD
Display message: Laptop price is: $550.0
"""



def laptopPrice():
    
    total = 0
    
# Reading user selections
    
    print("\n13.3          ---> 1")
    print("15.0          ---> 2")        
    print("17.3          ---> 3")
    screenSize = int(input("Select your screen size : \t"))
    if screenSize == 1:
        total += 200
    elif screenSize == 2:
        total += 300
    elif screenSize ==3:
        total += 400
        
    print("\ni3            ---> 1")
    print("i5             ---> 2")        
    print("i7             ---> 3")
    cpuType = int(input("Select your CPU type : \t"))
    if cpuType == 1:
        total += 150
    elif cpuType == 2:
        total += 250
    elif cpuType ==3:
        total += 350
        
    ramSize = int(input("Please enter RAM size : \t"))
    total += (ramSize/4) * 50

    print("\nHDD            ---> 1")
    print("SDD             ---> 2")        
    memoryType = int(input("Select your memory type: \t"))
    memorySize = int(input("Enter memory size          : \t"))  
    if memoryType == 1:
        total += (memorySize / 500) * 50
    elif memoryType == 2:
        total += (memorySize / 500) * 100

    print("\nFULLHD            ---> 1")
    print("4K                    ---> 2")        
    screenResolution = int(input("Select your screen resolution : \t"))
    if screenResolution == 1:
        total += 100
    elif screenResolution == 2:
        total += 200

    print("\nLaptop Price is : $", total)

# MAIN
    
laptopPrice()













