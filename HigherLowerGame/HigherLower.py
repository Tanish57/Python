from higherlowerart import logo, vs
from game_data import data
import random
import os
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def format_data(account):
  """Takes the account data and returns a printable format."""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"  # this when evaluated will return true if guess == a else false
  else:
    return guess == "b"

#Display Art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeatable.
while game_should_continue:

  # Generate a random account from the game data.

  # Making account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  # Ask user for guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is correct
  ## get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  # clear the screen between rounds.
  clear()
  print(logo)
  # giver user feedback on their guess.
  # Score keeping.
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")



