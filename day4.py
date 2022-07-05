# import random

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# length = len(names)

# personNo = random.randint(0, length-1);
# person = names[personNo]
# print(f"{person} is going to buy the meal today!")

# fruits = ["Strawberries", "nectarines", "Apples"]
# veggies = ["Spinach", "Kale", "Tomatoes"]

# dirty_dozen = [fruits, veggies]
# print(dirty_dozen[0])
# print(dirty_dozen[1])

# print(dirty_dozen[1][1])

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# row = int(position[0])
# col = int(position[1])


# map[row-1][col-1] = "X"
# # map[1][2] = 'X'


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if userChoice >= 3 or userChoice < 0:
  print("You typed and invalid number you lose")
else:
  print(game_images[userChoice])
  
  computerChoice = random.randint(0,2)
  print(f"Computer chose: ")
  print(game_images[computerChoice])
  
  
  if userChoice == 0 and computerChoice == 2:
    print("You win!!")
  elif computerChoice > userChoice:
    print("You lose!")
  elif computerChoice == userChoice:
    print("It's a draw")
  elif computerChoice == 0 and userChoice == 2:
    print("You lose")
  elif userChoice > computerChoice :
    print("You win!")
