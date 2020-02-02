seconds = int(input("Please enter the seconds: "))
hours = seconds//3600
minutes = (seconds%3600)//60
second = (seconds%3600)%60
print(f"{seconds} seconds= {hours} hours, {minutes} minutes, and {second} seconds")
