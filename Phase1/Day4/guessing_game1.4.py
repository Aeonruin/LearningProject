import random

secret_number = random.randint(1,600)
guess = 0
attempts = 1
max_attempts = 15
print("Welcome to Mike's number guessing game! Choose your difficulty.")
print("1. Easy [1-50]")

while True:
    guess = int(input("What number will you choose? "))
    print(f"Attempts Remaining: {max_attempts-attempts}")
    attempts += 1
    if guess == secret_number:
        print("You win!")
        answer = input("Would you like to go another round? (y/n) ")
        if answer == "n":
            break
        if answer == "y":
            secret_number = random.randint(1,600)
            attempts = 1
    elif guess > secret_number:
        print("You're guess is too high, a little lower.")
    elif guess < secret_number:
        print("You're guess is so small, a little higher.")
    if attempts >= max_attempts:
        print(f"You lose! the number was {secret_number}")
        answer = input("Would you like to go another round? (y/n) ")
        if answer == "n":
            break
        if answer == "y":
            secret_number = random.randint(1,600)
            attempts = 1
