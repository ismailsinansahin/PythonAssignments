def simpleRoomBook(availability, month, day, year):
    
    if availability and year==2018:
        if month ==7 and day<=8 and day>=1:            
            return False
        else:
            return True
    else:
        return False  
    
availability = int(input("Is there any room available / '1' for True / '0' for False :"))    
month = int(input("Enter the month : "))
day = int(input("Enter the day : "))
year = 2018    

print(simpleRoomBook(availability, month, day, year))


# Is there any room available / '1' for True / '0' for False :1
# Enter the month : 6
# Enter the day : 9
# True

# Is there any room available / '1' for True / '0' for False :1
# Enter the month : 7
# Enter the day : 5
# False

# Is there any room available / '1' for True / '0' for False :0
# Enter the month : 6
# Enter the day : 6
# False