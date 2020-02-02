seconds = int(input("Please enter the seconds: "))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = ((seconds % 86400) % 3600 ) // 60
second = ((seconds % 86400) % 3600) % 60
print(f"{seconds} seconds = {days} days, {hours} hours, {minutes} minutes, and {second} seconds")