year = int(input("Please enter a year: "))
if year%4==0 and year%100!=0  :
    print(year, "Leap Year")
elif year%100==0 and year%400==0 :
    print(year, "Leap Year")
else :
    print(year, "NOT a Leap Year")
    
    
    
    
    
    
    
    