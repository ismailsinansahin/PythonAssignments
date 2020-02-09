def validateTask(task, currentId, nextId):
    
    if task and currentId == nextId - 1:
        return True
    else:
        return False  
    
task = int(input("Is there any job in the task / '1' for True / '0' for False :"))    
currentId = int(input("Enter the current ID : "))
nextId = int(input("Enter the next ID : "))    
print(validateTask(task, currentId, nextId))


# Is there any job in the task / '1' for True / '0' for False :1
# Enter the current ID : 2
# Enter the next ID : 3
# True

# Is there any job in the task / '1' for True / '0' for False :1
# Enter the current ID : 8
# Enter the next ID : 7
# False

# Is there any job in the task / '1' for True / '0' for False :0
# Enter the current ID : 2
# Enter the next ID : 3
# False