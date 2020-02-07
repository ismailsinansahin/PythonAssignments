player = int(input("Please enter the total number of the cards of the player: "))
house = int(input("Please enter the total number of the cards of the house: "))

if player>21:
    print("bust")
elif house>player:
    print("player loss")
elif player==house:
    print("it is a tie")
elif player>house:
    print("player wins")