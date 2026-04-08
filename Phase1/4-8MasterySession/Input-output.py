name = input("Enter your name adventurer: ")
age = int(input("Current age: "))
class_list = ["Warrior","Mage","Healer","Ranger"]

while True:
    if age <= 17:
        print(f"You're too young, try again in {18 - age} year/years.")
        break
    elif age >=18:
        print(f"Welcome {name}!")
        print(class_list)
        choice = input("Choose your class:")
    if choice in class_list:
        print(f"You chose {choice}, Good luck adventurer!")
        break
