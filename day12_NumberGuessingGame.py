import random
print("Welcome to the Number Guessing Game!")

print("I'm Thinking of a number between 1 and 100")

randomNo = random.randint(0,100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if  difficulty == "easy":
    i = 10
    while(i>0):
        print(f"You have {i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess : "))
        if user_guess == randomNo:
            print("You guessed the correct number")
            break
        elif user_guess > randomNo:
            print("Too High")
            i-=1
        else:
            print("Too Low")
            i-=1

elif difficulty == "hard":
    i = 5
    while(i>0):
        print(f"You have {i} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess : "))
        if user_guess == randomNo:
            print("You guessed the correct number")
            break
        elif user_guess > randomNo:
            print("Too High")
            i-=1
        else:
            print("Too Low")
            i-=1
else:
    print("Invalid Selection")