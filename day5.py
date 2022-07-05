# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


n = 0
total_height = 0

for students in student_heights:
    total_height += students
    n += 1

avg_height = round(total_height / n)

print(avg_height)


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max = -100

for score in student_scores:
    if score > max:
        max = score

print(f"The highest score in the class is: {max}")


#Write your code below this row 👇

evensum = 0
for number in range(2, 101, 2):
    evensum += number

print(evensum)

#Write your code below this row 👇

for number in range(1, 101):
    if(number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif(number % 5 == 0):
        print("Buzz")
    elif(number % 3 == 0):
        print("Fizz")
    else:
        print(number)



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# hardpass = random.sample(password, len(password))
# hardpassword = "".join(hardpass)
# print(hardpassword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)
hardpass = ""
for char in password_list:
  hardpass += char

print(hardpass)