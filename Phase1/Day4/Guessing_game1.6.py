import random

max_attempts = 15
guess = 0
guess2 = 0
choice = 0
attempts = 0
difficulty = 100
staying = 0
stay = 0
num = random.randint(1, difficulty)
num2 = random.randint(1, difficulty)
print("Welcome to the Mario Party, we guessing numbers again. Choose your difficulty.")
while True:
    print("1.Normal: 1-100")
    print("2.Hard: 1- 500")
    choice = int(input("What will it be?: "))
    if choice == 1:
        difficulty = 100
        max_attempts = 25
    elif choice == 2:
        difficulty = 500
        max_attempts = 15
    else:
        print("Invalid number. defaulting to Very Hard.")
        difficulty = 1000
        max_attempts = 30
    while attempts < max_attempts:
        print(f"Challenge: {difficulty} Attempts: {max_attempts}")
        guess = int(input("Guess the first number: "))
        if guess == num:
            print("Correct! one more to go!")
            attempts += 0
            while attempts < max_attempts:
                guess2 = int(input("Guess the Second number: "))
                if guess2 == num2:
                    print("Correct! You win!")
                    attempts += 0
                    staying = input("Would you like to play again? Y or N: ")
                    if staying == "Y" or "Yes":
                        attempts = 0
                    elif staying == "N" or "No":
                        break
                if guess2 < num2:
                    print("Too low!, Try higher!")
                    attempts += 1
                    print(f"attempts remaining:{max_attempts - attempts}")
                if guess2 > num2:
                    print("Too high!, lower, Lower!")
                    attempts += 1
                    print(f"attempts remaining:{max_attempts - attempts}")
                if attempts >= max_attempts:
                    staying = input(f"You lose the number was {num2}! Would you like to play again? Y or N: ")
                    if staying == "Y" or "Yes":
                        attempts = 0
                        continue
                    elif staying == "N" or "No":
                        break
            while True:
                staying = input("Would you like to play again? Y or N: ")
                if staying == "Y" or "Yes":
                    attempts = 0
                    continue
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
            stay = int(input(f"You lose the number was {num}, Would you like to play again? Y or N: "))
            if stay in ("Y","Yes"):
                attempts = 0
                continue
            elif stay in ("N","No"):
                break
    else:
        print("Invalid number.")
