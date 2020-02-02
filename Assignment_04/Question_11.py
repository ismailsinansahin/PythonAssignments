medium = input("Please enter the medium that your sound go through: air, water, or steel : --> ")
distance = int(input("Please enter the distance that the sound go: "))
if medium == 'air':
    time = distance / 1100
elif medium == 'water':
    time = distance / 4900
elif medium == 'steel':
    time = distance / 16400
else:
    print("invalid input")  
print("Time=", time)
