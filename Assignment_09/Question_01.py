"""
Create a method called tipCalculator which accepts parameters:  
boolean isSplit, int numberPeople, double checkAmount, String serviceQuality
Ask the user to enter each value. 
User should select service quality that will correspond to tip percent.
    Poor = 5%
    Fair = 10%
    Good = 15%
    Great = 20%
    Excellent = 25%

Input: 
    Split:Yes
    Number of people:4
    Check amount:476.0
    Service Quality:Excellent

The program should display the following information based on the user input: 
    Output:
    Split or No split
    Number of people entered: &&&&
    Service Quality:
    Total to pay: 595.0
    Total tip: 119.0
    Total per person: 148.75
    Tip per person: 29.75
"""

def tipCalculator():
    
    # Reading data from user
    
    print("\nYes  ---> 1")
    print("No    ---> 2")
    isSplit = int(input("Will you share the check? \t"))
 
    if isSplit == 1:
        numberPeople = int(input("Howmany people will share? \t"))
    else:
        numberPeople = 1
        
    checkAmount = int(input("What is your check amount? \t"))
            
    print("\nPoor           ---> 1")
    print("Fair           ---> 2")        
    print("Good           ---> 3")
    print("Great         ---> 4")           
    print("Excellent  ---> 5")
    serviceQuality = int(input("How did you find our service? \t"))
    
    # Making calculations
    
    tip = checkAmount * serviceQuality * 5 / 100  
    totalToPay = checkAmount + tip
    totalPerPerson = totalToPay / numberPeople  
    tipPerPerson = tip / numberPeople
    
    # Printing results
    
    if isSplit == 1:
        print("\nSplit                                 : Yes")
    else:
        print("Split                                 : No")
        
    print("Number of people entered  :", '&' * numberPeople)
    
    if serviceQuality == 1:
        print("Service Quality                : Poor")    
    elif serviceQuality ==2:
        print("Service Quality                : Fair")  
    elif serviceQuality == 3:
        print("Service Quality                : Good")  
    elif serviceQuality == 4:
        print("Service Quality                : Great")  
    elif serviceQuality == 5:
        print("Service Quality                : Excellent")  
        
    print("Total to pay                      :", totalToPay)
    print("Total tip                           :", tip)
    print("Total per person               :", totalPerPerson)
    print("Tip per person                   :", tipPerPerson)
   
# MAIN    BODY 

tipCalculator()
    

