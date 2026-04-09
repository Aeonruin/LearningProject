while True:
    answer = input("Welcome to the number doubler! would you like to... you know? double that number? ")
    if answer in ("yes", "y"):
        while True:
            num = int(input("State your number peasant: "))
            print(f"and your answer is: {num * 2}")
            if num == 0:
                print("Returning to main menu")
                break

    if answer in ("no","n"):
                print("not a problem at all! have a good day!")
                break
