weightPound = int(input("Please enter your weight: "))
heightFeet = int(input("Please enter your heights feets portion: "))
heightInches = int(input("Please enter your heights inches portion: "))
weight = weightPound/2.2
height = ((heightFeet*12)+(heightInches))*0.0254
BMI = weight/(height*height)
print(f"Your weight is {weight} kg")
print(f"Your height is {height} m")
print(f"Your BMI is {BMI}")

if BMI<18.5 :
    section = "Underweight"
elif 18.5<=BMI<25 :
    section = "Normal Weight"
elif 25<=BMI<30 :
    section = "Overweight"
else :
    section = "Obese"
    
print(f"Your risk factory is {section}")