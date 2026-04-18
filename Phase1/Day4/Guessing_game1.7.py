import random

attempts = 0
max_attempts = 10
difficulty = 1
stay = 0
stage = 1
playing = True

while playing == True:
    print("Welcome once again to the game that never ends, Choose your difficulty.")
    print("1.Norma1: 100 words, 15 attempts")
    print("2.Hard: 500 words, 15 attempts")
    choice = int(input("Choose your difficulty: "))
    attempts = 0
    stage = 1
    if choice == 1:
        difficulty = 100
        max_attempts = 15
    elif choice == 2:
        difficulty = 500
        max_attempts = 20
    else:
        print("Wrong selection, Dafaulting to medium.")
        difficulty = 250
        max_attempts = 15
    secret_number1 = random.randint(1, difficulty)
    secret_number2 = random.randint(1, difficulty)
    while attempts < max_attempts:
        if stage == 1:
            guess = int(input("Choose the first number: "))
            if guess == secret_number1:
                print("Correct! on to the next!")
                stage = 2
                continue
            elif guess < secret_number1:
                print("Too low.")
                attempts += 1
                print(f"Attempts Remaining: {max_attempts - attempts}")
            elif guess > secret_number1:
                print("Too high.")
                attempts += 1
                print(f"Attempts Remaining: {max_attempts - attempts}")
        elif stage == 2:
            guess2 = int(input("Now! Coose the second number: "))
            if guess2 == secret_number2:
                print("YOU WIN! flawless Victory!")
                stay = input("Would you like to play again?: ")
                if stay.lower()  in ("Yes", "Y"):
                    break
                else:
                    print("Goodbye!")
                    playing = False
            elif guess2 < secret_number2:
                print("Too low.")
                attempts += 1
                print(f"Attempts Remaining: {max_attempts - attempts}")
            elif guess2 > secret_number2:
                print("Too high.")
                attempts += 1
                print(f"Attempts Remaining: {max_attempts - attempts}")
        if attempts >= max_attempts:
            stay = input("Nice try! you've expended your attempts. would you like to play again? ")
            if stay.lower()  in ("Yes", "Y"):
                playing = True
            elif stay.lower()  in ("No", "N"):
                print("Goodbye!")
                playing = False
