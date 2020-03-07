"""
Write a program that will calculate car insurance premium.

Steps to write a program:
    
First things first, your program should ask the customer to provide a name, so 
display a message: "Enter your name".

Then ask the user about ownership of the US driver's license. 
Display message: "Do you have a US driver license?".
    If the user doesn't have a US driver's license - display warning message: "Invalid data!" 
    and stop the program (use System.exit(0) after displaying warning message to stop the program).

Then ask the user to provide a zip code. 
    If zip code equals to 20910 or 20740, add $60 to the premium (an amount to be paid for an insurance policy).
    If zip code equals to 22102 or 22103, add $30 to the premium. Otherwise, add $50 to the premium.

Then ask the user about car ownership. 
Display message: "Is this vehicle Owned, Financed, or Leased?". 
    If the car is owned, add $10 to the premium, otherwise, add $20 to the premium.

Then ask the user about car usage.
 Display message: "How is this vehicle primarily used?". 
    If the car used for Business, add $50 to the premium.
    If the car is for pleasure add $10 to the premium. ,
    If the car is for Commute - add $20 to the premium.

Then ask the user how many days per week user drives to work. 
Display message: "Days Driven To Work And/Or School".
    Add $5 to the premium for every day driven to work.

Then, ask the user about how many miles customers drive to work or school. 
Display message: "Miles Driven To Work And/Or School". 
    Increase premium per $1 for every 1 mile.

Then ask the customer about his age. Display message: "How old are you?". 
    If age is less than 16, display the message: "Invalid data!", and stop the program.
    If age is between 16 and 18 (exclusive), multiply premium by 20. 
    If age is between 18 (inclusive) and 21 (inclusive), multiply premium by 6. 
    If age is between 21 (exclusive) and 25 (exclusive), multiply premium by 2.

Then, ask the customer about the driving experience.
Make sure that experience is greater than 0 and the result of subtraction age from experience is 
greater or equals to 16. If no, display the message: "Invalid data!" and stop the program. 
    Reduce premium on $5 for every year of experience.

Then, ask the customer about car accidents. 
Display message: "Have you had any accidents in the last 5 years?". 
    If the answer equals "Yes" or "YES", ask customer about amount of accidents. 
    Display message: "How many?", in order to get information about the amount of accidents. 
    Add 20% to the premium price for every accident.

Then, ask the customer if he had continuous insurance for the past 12 months. 
Display message: "Have you had continuous insurance for the past 12 months?". 
    If the customer provides a negative answer (No) - double the premium.

Then ask the user about the level of education. 
Display message: "What is the highest level of education you have completed?". 
    If the level of education equals to "Ph.D." or "Bachelors" or "Masters" - reduce the premium by 5%. 
    If the level of education equals "Doctors" reduce the premium by 10%. 
    If the level of education equals "Less than High School" increase the premium by 5%.

After all, display the message "customer, here's your quote!". 
    Instead of the customer, you need to insert customers' name. 
    The display message: "Start Your Policy Today For: $premium".
    Instead of premium, your program should print the premium's variable value. 
    Then display the message with reference number: "Reference number: referenceNumber". 
    In order to build reference number variable (referenceNumber), 
    concatenate first 2 letters of customer's name, age, last 2 letters of customer's name, zip code, 
    and level of education without spaces. This value should be all upper case!

Sample Output:
    Display message: David, here's your quote!
    Display message: Start Your Policy Today For: $52.25
    Display message: Reference number: DA25ID20910PHD
"""
import sys
premium = 0;
flag = True

name = input("\nPlease enter your name : ")

while flag == True:
    print("\n1 .... Yes")
    print("2 .... No")
    USDriverLicense = input("Do you have a US driver license? (1, 2): ")
    if USDriverLicense == "1":
        flag = False
    elif USDriverLicense == "2":
        print("Invalid data!")
        sys.exit()
    else:
        flag = True

flag = True
zipCode = input("Please enter your zip code : ")
if zipCode == "20910" or zipCode == "20740":
    premium += 60
elif zipCode == "22102" or zipCode == "22103":
    premium += 30
else:
    premium += 50
    
print("\nPremium : ", premium)
         
while flag == True:
    print("\n1 .... Owned")
    print("2 .... Financed")
    print("3 .... Leased")
    ownership = input("Is this vehicle Owned, Financed, or Leased? (1, 2, 3): ")  
    if ownership == "1":
        premium += 10
        flag = False
    elif ownership == "2" or ownership == "3":
        premium += 20
        flag = False
    else:
        flag = True

flag = True       
print("\nPremium : ", premium)
 
while flag == True:
    print("\n1 .... Business")
    print("2 .... Pleasure")
    print("3 .... Commute")
    usage = input("How is this vehicle primarily used? : ")  
    if usage == "1":
        premium += 50
        flag = False
    elif usage == "2":
        premium += 10
        flag = False
    elif usage == "3":
        premium += 20
        flag = False
    else:
        flag = True
 
flag = True
print("\nPremium : ", premium)

daysPerWeek = int(input("Days Driven To Work And/Or School : "))
milesTo = int(input("Miles Driven To Work And/Or School : "))
premium += (daysPerWeek * 5) + (daysPerWeek * milesTo * 1)

print("\nPremium : ", premium)

age = int(input("How old are you? : "))
if age < 16:
    print("Invalid data")
    sys.exit()
elif 16 <= age < 18:
    premium *= 20
elif 18 <= age <= 21:
    premium *= 6
elif 21 < age < 25:
    premium *= 2
    
print("\nPremium : ", premium)

experience = int(input("Howmany years of driving experience do you have? : "))
if experience == 0 or age-experience < 16:
    print("Invalid data")
    sys.exit()
else:
    premium -= experience * 5

print("\nPremium : ", premium)

while flag == True:
    print("\n1 .... Yes")
    print("2 .... No")
    anyAccident = input("Have you had any accidents in the last 5 years : ")
    if anyAccident == "1":
        accidentNumber = int(input("Howmany accidents have you had in the last 5 years? : "))
        premium += premium * 0.20 * accidentNumber
        flag = False
    elif anyAccident == "2":
        flag = False
        continue
    else:
        flag = True

flag = True        
print("\nPremium : ", premium)

while flag == True:
    print("\n1 .... Yes")
    print("2 .... No")
    contInsurance = input("Have you had continuous insurance for the past 12 months? : ")
    if contInsurance == "1":     
        flag = False
    elif contInsurance == "2":
        premium += premium * 2
        flag = False
        continue
    else:
        flag = True

flag = True        
print("\nPremium : ", premium)

while flag == True:
    print("\n1 .... Ph.D. / Bachelors / Masters")
    print("2 .... Doctors")
    print("3 .... Less than High School")
    education = input("What is the highest level of education you have completed? (1, 2, 3): ")  
    if education == "1":
        premium -= premium * 0.05
        flag = False
    elif education == "2":
        premium -= premium * 0.10
        flag = False
    elif education == "3":
        premium += premium * 0.05
        flag = False
    else:
        flag = True

flag = True        
print("\nPremium : ", premium)

print("\n", name, ", here is your quote!")
print("Start Your Policy Today For: $", premium)
print("Referance number: ", name[0:2].upper(), age, name[-2:].upper(), zipCode, education.upper(), sep="")



    
    
    
    
    
    
    
    
    
    
    