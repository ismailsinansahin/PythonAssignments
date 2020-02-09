def c_profits(buyPrice, sellPrice):
    if buyPrice>sellPrice:
        return "loss"
    if sellPrice>buyPrice:
        return "profit"
    if sellPrice==buyPrice:
        return "no loss"
    
sellPrice = int(input("Please enter the sell price : "))
buyPrice = int(input("Please enter the buy prices  : "))
print("c_profits(", buyPrice, ",", sellPrice, ")", sep="")
print("returns : ", c_profits(buyPrice, sellPrice))


# c_profits(100,1500)
# returns :  profit

# c_profits(20,5)
# returns :  loss

# c_profits(100,100)
# returns :  no loss
