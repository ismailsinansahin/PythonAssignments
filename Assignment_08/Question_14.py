def threeLocks(a,b,c):
    
    if (a and b) or c:
        return True
    else:
        return False

a = int(input("First boolean   / '1' for True / '0' for False - a - : "))
b = int(input("Second boolean  / '1' for True / '0' for False - b - : "))
c = int(input("Third boolean   / '1' for True / '0' for False - c - : "))        
print(threeLocks(a,b,c))

# First boolean   / '1' for True / '0' for False - a - : 1
# Second boolean  / '1' for True / '0' for False - b - : 0
# Third boolean   / '1' for True / '0' for False - c - : 1
# True

# First boolean   / '1' for True / '0' for False - a - : 1
# Second boolean  / '1' for True / '0' for False - b - : 1
# Third boolean   / '1' for True / '0' for False - c - : 0
# True

# First boolean   / '1' for True / '0' for False - a - : 0
# Second boolean  / '1' for True / '0' for False - b - : 0
# Third boolean   / '1' for True / '0' for False - c - : 0
# False