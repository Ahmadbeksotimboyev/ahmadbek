import random 
# import module

# random_integer = random.randint(1,19)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
# random_float * 5

states_of_america = ["Delaware","Pennsylvania"]

# states_of_america.append("Angelaland")

# states_of_america.extend(["Angelaland","JackBauer Land"])
# print(states_of_america[0])
# names = "Ahmadbek"

# num_items = len(names)

# random_choice = random.randint(0,num_items - 1)
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + "is going to buy the meal today!")

# states_of_america[1] = "Pencilvania"

# states_of_america.extend(["Angelaland","JackBauer Land"])

# print(states_of_america)


# dirty_dozen = ["Strawberries", "Sninach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes","Celery","Potatoes"]

# fruits = ["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " "]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? :")

# horizonal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizonal - 1] = "X"

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

compyuter_choice = random.randint(0, 2)
print(f"Compyuter chose {compyuter_choice}")

if user_choice == 0 and compyuter_choice == 2:
    print("you win!")
elif compyuter_choice > user_choice:
    print("You lose")
elif compyuter_choice > user_choice:
    print("You lose!")
elif user_choice > compyuter_choice:
    print("You win!")
elif compyuter_choice == user_choice:
    print("It's a draw")
elif user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose")