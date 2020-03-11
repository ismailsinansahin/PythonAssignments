"""
A slot machine (Links to an external site.) is a gambling device that the user inserts money into 
and then pulls a lever (or presses a button). The slot machine then displays a set of random images. 
If two or more of the images match, the user wins an amount of money that the slot machine dispenses 
back to the user.
Create a program that simulates a slot machine. When the program runs, it should do the following:
Ask the user to enter the amount of money he or she wants to enter into the slot machine.
Instead of displaying images, the program will randomly select a word from the following list: 
Cherries, Oranges, Plums, Bells, Melons, Bars
To select a word, the program can generate a random number in the range of 0 through 5. 
If the number is 0, the selected word is Cherries; if the number is 1, 
the selected word is Oranges; and so forth. 
The program should randomly select a word from the list three times and display all three of the words.
If none of the randomly selected words match, the program will inform the user that he or she has won $0.
If two of the words match, the program will inform the user that 
he or she was won two times the amount entered.
If three of the words match, the program will inform the user that 
he or she has won three times the amount entered.
The program will ask whether the user wants to play again. 
If so, these steps are repeated. If not, the program displays the total amount of money 
entered into the slot machine and the total amount won.
"""

import random

images = ["Cherries", "Oranges", "Plum",  "Bells", "Melons", "Bars"]

totalMoneyEntered = 0
totalWon = 0
cont = True

while cont == True:
    
    luckyImages = []
    
    bidMoney = int(input("How much money do you want to bid: "))
    totalMoneyEntered += bidMoney
    
    for i in range(3):
        i = random.randint(0,5)
        luckyImages.append(images[i])
    
    print(luckyImages)
    
    if luckyImages[0] == luckyImages[1] == luckyImages[2]:
        wonMoney = bidMoney * 3
    elif luckyImages[0] == luckyImages[1] or  luckyImages[0] == luckyImages[2] or  luckyImages[1] == luckyImages[2]:
        wonMoney = bidMoney * 2
    else:
        wonMoney = 0
        
    print("You won : ", wonMoney)
    totalWon += wonMoney
    
    print(f"\nYou totally entered : {totalMoneyEntered}")
    print(f"Finally you have          : {totalWon}")
    
    a = input(print("\nPress 1 if you want to play again : "))
    if a != "1":
        cont = False
        
print("Thank you for playing ...")


    
    
    
    
    
    
    
    
    
    
    
    
