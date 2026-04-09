attempts = 1
max_attempts = 20
import random
secret_number = random.randint(1,600)
guess = 0
print("Welcome to the numbers guessing game!")
while True:
    guess = int(input("Guess the number: "))
    print(f"Attempts: {max_attempts - attempts}")
    if guess == secret_number:
        print("You win!")
        break
    if guess < secret_number:
        print("You're far too low!")
        attempts += 1
    elif guess > secret_number:
        print("You're too high!")
        attempts += 1
    elif attempts >= max_attempts:
        print(f"You lose, the answer was {secret_number}")
        break

