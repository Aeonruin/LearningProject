import random

max_number = 1
guess = 0
attempts = 0
max_attempts = 0
secret_number = random.randint(1, max_number)
print("Welcome to Mike's number guessing game! Choose your difficulty.")
print("1. Easy [1-50]")
print("2. Medium [1-200]")
print("3. Hard [1-600]")
choice = input("1,2, or 3: ")
if choice == "1":
    max_number = 50
    max_attempts = 10
elif choice == "2":
    max_number = 200
    max_attempts = 12
elif choice == "3":
    max_number = 600
    max_attempts = 15
else:
    print("Invalid choice, defaulting to Medium.")
    max_number = 200
while True:
    print(f"Pick a number between 1 and {max_number}.")
    guess = int(input("What number will you choose? "))
    print(f"Attempts Remaining: {max_attempts-attempts}")
    attempts += 1
    if guess == secret_number:
        print("You win!")
        answer = input("Would you like to go another round? (y/n) ")
        if answer == "n":
            break
        if answer == "y":
            secret_number = random.randint(1, max_number)
            attempts = 1
            print("1. Easy [1-50]")
            print("2. Medium [1-200]")
            print("3. Hard [1-600]")
            choice = input("1,2, or 3: ")
            if choice == "1":
                max_number = 50
                max_attempts = 10
            elif choice == "2":
                max_number = 200
                max_attempts = 12
            elif choice == "3":
                max_number = 600
                max_attempts = 15
            else:
                print("Invalid choice, defaulting to Medium.")
                max_number = 200
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
            secret_number = random.randint(1, max_number)
            attempts = 1
            print("1. Easy [1-50]")
            print("2. Medium [1-200]")
            print("3. Hard [1-600]")
            choice = input("1,2, or 3: ")
            if choice == "1":
                max_number = 50
                max_attempts = 10
            elif choice == "2":
                max_number = 200
                max_attempts = 12
            elif choice == "3":
                max_number = 600
                max_attempts = 15
            else:
                print("Invalid choice, defaulting to Medium.")
                max_number = 200
        else:
            print("invalid selection, ending")
            break
    else:
        print("Invalid number.")