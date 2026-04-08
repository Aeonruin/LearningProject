while True:
    num = int(input("Give me a number? "))

    if num == 0:
        print("You chose to end. Goodbye!")
        break

    for i in range(1, num + 1):
        if i % 2 == 0:
            print(i)
