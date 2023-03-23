#syntax for dict comprehension
# new_dict = {new_key : new_value for item in list} # dict comprehension using a list

#syntax for dictionary comprehension using a dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random
student_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student:marks for (student, marks) in student_scores.items() if marks >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
words = sentence.split()

result = {word:len(word) for word in words}

# or simply result = {word:len(word) for word in sentence.split()}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day:(temp * 9/5)+32 for (day, temp) in weather_c.items()}

print(weather_f)