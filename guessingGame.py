import random
#get the user's guess
guess = int(input("Enter your guess between 1 and 100: "))

randnum = randint(1, 101)

if guess < randnum:
    print("higher")
elif guess > randnum:
    print("lower")
else:
    print("You guessed it!")