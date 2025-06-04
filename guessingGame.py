import random
#get the user's guess

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count
    
        elif guess > randnum:
            count +=1
            return computerGuess(lowval, guess - 1, randnum, count)
        else:
            count += 1
            return computerGuess(guess + 1, highval, randnum, count)
    else:
        return -1

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
print(f"The computer took  {computerGuess(1, 100, randnum)} tries!")
       