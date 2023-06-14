import random
number = random.randint(1,100)
guess=0
while guess!=number:
    guess = int(input("Guess a number:"))
    if guess<number:
        print("You loose! \nNumber is low")
    elif guess>number:
        print("You loose! \nNumber is High")
    else:
        print("You Won!")
        break