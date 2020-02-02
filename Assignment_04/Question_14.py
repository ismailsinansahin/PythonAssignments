books = int(input("Howmany books you purchased this month: "))

if books == 0:
    points = 0
elif books == 1:
    points = 5
elif books == 2:
    points = 15
elif books == 3:
    points = 30
elif books >=4:
    points = 60

print(f"Your purchased {books} books this month and you get {points} points.")
