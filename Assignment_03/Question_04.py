# The easiest way in Python
num1=1
num2=2
print(f"Num1= {num1} Num2= {num2}")
num1,num2=num2,num1
print(f"Num1= {num1} Num2= {num2}")

# The way which using third variable
num3=3
num4=4
print(f"Num3= {num3} Num4= {num4}")
num7=num3
num3=num4
num4=num7
print(f"Num3= {num3} Num4= {num4}")

# The way which using only arithmetic operations
num5=5
num6=6
print(f"Num5= {num5} Num6= {num6}")
num5=num5+num6
num6=num5-num6
num5=num5-num6
print(f"Num5= {num5} Num6= {num6}")