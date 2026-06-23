#!/usr/bin/env python3
from numpy import random
import sys

print("This is an interactive geussing game !\nYou have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.\nGood lick !\n")
secret = random.randint(1,99)
count = 1
while True:
    print("What's your guess between 1 and 99?")
    guess = input(">> ")
    if guess == "exit":
        print("Goodbye!")
        sys.exit()
    else:
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number")
            continue
    if guess != secret:
        if guess > secret:
            print("Too high!")
            count +=1
            continue
        if guess < secret:
            print("Too low!")
            count += 1
            continue
    else:
        if secret == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if count == 1:
            print("Congratulations! You got it on your first try!")
            sys.exit(0)
        else:
            print(f"Congratulations, you've got it!\nYou won in {count} attempts!")
            sys.exit(0)
    
    


