import random


number_to_guess = random.randint(1, 100)

user_guess = None

while user_guess != number_to_guess:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    if user_guess != number_to_guess:
        print("Try again")
    else:
        print("Congrats. You guessed the number!")