calls = int(input("Please enter the number of call: "))
if calls <= 100 :
    bill = 200
elif 100 < calls <= 150 :
    bill = 200 + ((calls - 100) * 0.60)
elif 150 < calls <= 200 :
    bill = 200 + (50 * 0.60) + ((calls - 150) * 0.50)
elif calls > 200 :
    bill = 200 + (50 * 0.60) + (50 * 0.50) + ((calls - 200) * 0.40)
print("Your bill is : ", bill)
