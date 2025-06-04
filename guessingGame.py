import random
#get the user's guess

randnum = random.randint(1, 101)

count = 0
guess = 0
while guess != randnum:
    guess = int(input("Enter your guess between 1 and 100: "))
    if guess < randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("You guessed it!")
        break
    count += 1
print(f"You guessed it in {count} tries!")
       