attempts = 1
max_attempts = 20
print("Welcome to Guess that word!")
while True:
    guess = input("First guess, it's public transport has a set rounte. what it is? ").lower().strip()
    print(f"Attempts Remaining: {max_attempts - attempts}")
    if guess == "bus":
        attempts -=1
        while True:
            guess = input("Great! Second question, it's an animal. a long one sometimes has poison? ").lower().strip()
            print(f"Attempts Remaining: {max_attempts - attempts}")
            if guess == "snake":
                print("You win!")
                break
            else:
                attempts += 1
    else:
        attempts += 1
    if attempts >= max_attempts:
        print("You lose")
        break

