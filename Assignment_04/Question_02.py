income = int(input("Please enter your income: "))/1000000

if income <= 150 :
    tax = income*0.25
elif income <=300 :
    tax = (150*0.25) + ((income-150)*0.30)
elif income <=600 :
    tax = (150*0.25) + (150*0.30) + ((income-300)*0.35)
elif income <=1200 :
    tax = (150*0.25) + (150*0.30) + (300*0.35) + ((income-600)*0.40)
else :
    tax = (150*0.25) + (150*0.30) + (300*0.35) + (600*0.40) + ((income-1200)*0.50)
    
print(f"Your income : {income*1000000}")
print(f"The tax amount you have to pay : {tax*1000000}")