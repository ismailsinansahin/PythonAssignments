caloriesTaken = int(input("Please enter the number of calories you ate: "))
fatGrams = int(input("Please enter the number of fat grams your food included: "))
fatCalories = fatGrams * 9
if fatCalories > caloriesTaken:
    print("Input is invalid")
else:
    percentageOfCalories = fatCalories / caloriesTaken
    print("Percentage of calories from fat is:", percentageOfCalories)
    if percentageOfCalories <= 0.30:
        print("Your food is low in fat")
