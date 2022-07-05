################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# print(potion_strength) can't access this outside the scope of this function
# we can access this outside the function using global scope

#Global Scope

player_health = 10

def drink_potion():
  global potion_strength
  #global scoping using the global keyword
  potion_strength = 2
  print(player_health)

drink_potion()
print(potion_strength)

#anything that you give name to has a namespace and that namespace is valid in certain scopes

#python does not have any block scope which means you can create a new variable inside a if-else block, while/for loop then this new variable would be accessible outside the if block/for/while loop throughout global namespace. but within a function it is not possible as within a funciton has a global scope

# to access the global variable inside a function:
# dushman = 1
# print(f"Initial Dushman : {dushman}")
# def increase():
#   global dushman
#   dushman += 1
#   print(f"dushman inside the function: {dushman}")

# increase()
# print(f"dushman outside the function: {dushman}")

# avoid modifying global scope within a function that has local scope, and if you want to change a global scope value using a function then use return value instead:

dushman = 1

print(f"Initial Dushman : {dushman}")

def increase():
  print(f"dushman inside the function: {dushman}")
  return dushman + 1
dushman = increase()  #updating the global dushman via updating it with the returned value of the function
print(f"dushman outside the function: {dushman}")

# Global Constants:
# global scope can be extremely useful especially when you're defining constants. Global Constants are variables you define and you're never planning on changing it ever again. It's just something like, for eg: the value of pi. You wanna look it up once and you want it into your code and you never want to look it up ever again

PI = 3.14159
URL = "https://www.google.com"
INSTAGRAM_HANDLE = "@tanish57"

# define all the global constants in UPPERCASE, that way when you see all CAPS variable you'll recognize that they're global constants and should not be changed
