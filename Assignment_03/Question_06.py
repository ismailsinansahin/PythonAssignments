lethalOverdose = 10000
cola = 34
coffee = 160
colaDrunk = int(input("Howmany can of cola did you drink: "))
coffeeDrunk = int(input("Howmany can of coffee did you drink: "))
consumedCola = cola*colaDrunk
consumedCoffee = coffee*coffeeDrunk
consumedTotal = consumedCoffee+consumedCola

if consumedTotal>10000 :
    print("You are already dead!")
else :
    print(f"Number of miligrams in drink: {consumedTotal}")
    print(f"It would take about {(10000-consumedTotal)//cola} can of cola or {(10000-consumedTotal)//coffee} for a lethal overdose!")
