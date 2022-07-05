# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if(height >= 120):
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before your can ride.")

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if number % 2 == 0 :
#     print("This is an even number")
# else:
#     print("This is an odd number")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")


# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# raw_bmi = weight / height ** 2
# bmi = round(raw_bmi)
# if(bmi < 18.5):
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif(bmi >= 18.5 and bmi <= 25):
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif(bmi > 25 and bmi < 30):
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif(bmi >= 30 and bmi <= 35):
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")



# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# if(year % 4 == 0):
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# name1_lower = name1.lower()
# name2_lower = name2.lower()

# T = name1_lower.count('t') + name2_lower.count('t')
# R = name1_lower.count('r') + name2_lower.count('r')
# U = name1_lower.count('u') + name2_lower.count('u')
# E = name1_lower.count('e') + name2_lower.count('e')

# true_count = T + R + U + E

# L = name1_lower.count('l') + name2_lower.count('l')
# O = name1_lower.count('o') + name2_lower.count('o')
# V = name1_lower.count('v') + name2_lower.count('v')
# E = name1_lower.count('e') + name2_lower.count('e')

# love_count = L + O + V + E

# score = str(true_count) + str(love_count)

# score_num = int(score)

# if(score_num <= 10 or score_num >= 90):
#     print(f"Your score is {score_num}, you go together like coke and mentos.")
# elif (score_num >= 40 and score_num <= 50):
#     print(f"Your score is {score_num}, you are alright together.")
# else:
#     print(f"Your score is {score_num}.")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

crossroad = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')

if(crossroad == "left"):
  lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
  if(lake == "wait"):
    island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? " )
    if(island == "red"):
      print("It's a room full of fire. Game Over.")
    elif(island == "yellow"):
      print("You found the treasure! You Win!")
    elif(island == "blue"):
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("Game Over.")

else:
  print("Game Over.")
