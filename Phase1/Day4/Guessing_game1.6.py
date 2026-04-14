import random

max_attempts = 15
guess = 0
guess2 = 0
choice = 0
attempts = 0
difficulty = 100
num = random.randint(1, difficulty)
num2 = random.randint(1, difficulty)
print("Welcome to the Mario Party, we guessing numbers again. Choose your difficulty.")
while attempts < max_attempts:
    print("1.Normal")
    print("2.Hard")
    choice = int(input("What will it be?: "))
    if choice == 1:
        difficulty = 100
        max_attempts = 15
    if choice == 2:
        difficulty = 500
        max_attempts = 10
        while True:
            guess = int(input("Guess the first number: "))
            if guess == num:
                print("Correct! one more to go!")
                attempts += 0
                guess2 = int(input("Guess the Second number: "))
                if guess == num2:
                    print("Correct! You win!")
                    attempts += 0
                    while True:
                        staying = input("Would you like to play again? Y or N: ")
                        if staying == "Y" or "Yes":
                            attempts = 0
                        elif staying == "N" or "No":
                            break
            elif guess < num:
                print("Too low, go higher!")
                attempts += 1
                print(f"attempts remaining:{max_attempts - attempts}")
            elif guess > num:
                print("Too high, bring it down!")
                attempts += 1
                print(f" attempts remaining:{max_attempts - attempts}")
            if attempts >= max_attempts:
                stay = int(input("Would you like to play again? Y or N: "))
                if stay in ("Y","Yes"):
                        attempts = 0
                elif stay in ("N","No"):
                    break
    else:
        print("Invalid number.")
