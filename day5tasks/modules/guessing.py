import random
import math
secret_number = random.randint(1, 50)
print("=== Number Guessing Game ===")
print("Guess the number between 1 and 50.")
print("You have 5 attempts.\n")
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    difference = math.fabs(secret_number - guess)
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print(f"Your guess is {difference:.0f} away from the correct number.")
        if attempt < 5:
            print("Try again!\n")
        else:
            print("\n Game Over!")
            print(f"The correct number was: {secret_number}")