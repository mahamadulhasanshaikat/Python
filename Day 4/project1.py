#Number gussing game

import random
# Random number between 1 and 50
number = random.randint(1, 50)
attempts = 0
guess = 0

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 50.")

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
