attempts = 0

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if password == "Python123":
        print(f"Password accepted! Welcome {username}!")
        break
    else:
        attempts += 1
        print("Incorrect password, try again.")

    if attempts > 10:
        print("Password not accepted! Closing.")
        break
