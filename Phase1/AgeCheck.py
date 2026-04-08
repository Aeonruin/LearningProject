name = input("What name can I take from you?")
age = int(input("How many summers are you~?"))

if age <= 13 :
    print(f"{age}? You are too young")
elif age <= 17 :
    print("Damn teen, keep studying you're almost there.")
else:
    print("You're an adult Homeskillet, this is good.")