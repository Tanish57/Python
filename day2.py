#Data Types

#String

print("Hello"[-1])

#Integer: numbers without any decimal places

print(123 + 345)

print(123_456_789)
#underscore is used to make large numbers more readable to humans, as we use commas to seperate large number, same way we can use underscore in python to seperate large numerical values

print(123_456.12)
#Float: numbers with decimal places

print(123.56)

# Boolean
True
False

num_char = len(input("Please enter your name: "))

print(type(num_char))

new_num_char = str(num_char)

print(type(new_num_char))

print("Your name has " + new_num_char +" characters")

a = float(123)
print(type(a))

b = str(123)
print(type(b))

print(70 + float("100.5"))
print(str(70) + str(100))


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
print(int(two_digit_number[0]) + int(two_digit_number[1]))

# Pemdas
# Parentheses
# Exponents
# Multiplication Division
# Addition Subtraction

eq = 3*(3+3)  / 3 - 3
print(eq)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = float(weight)/float(height)** 2

print(int(bmi))

print(round(8/3))

print(round(8/3 , 3))

# floor division: getting int straightaway with chopped of decimal values instead of flaoting point value, 

print(8 // 3) #datatype is integer

# f-string

score = 0
height = 1.8
isWinning = True
print(f"Your score is {score} and the height of player is {height}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
totaldays = 90 * 365
totalweeks = 90 * 52
totalmonths = 90 * 12

days_left = totaldays - (int(age) * 365)
weeks_left = 90 * 52 - (int(age) * 52)
months_left = 90 * 12 - (int(age) * 12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill_amt = float(input("what was the total bill? $"))
tip = int(input("10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill_amt + bill_amt

final_pay = bill_with_tip / people

final_amount = round(final_pay, 2)
final_amount = "{:.2f}".format(final_pay)

print(f"Each person should pay: ${final_amount}")
