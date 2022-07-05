programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running   as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Function"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something again and again."

print(programming_dictionary["Loop"]) 
print(programming_dictionary)

empty_dictionary = {}

# wipe and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "Keeda"
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])


# nesting a list and dictionary inside a dictionary
travel_log = {
  "France":{"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
  "Germany":{"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5}
}

print(travel_log)

# nesting a dictionary inside a list

travel_log = [
  {
    "country" :"France" ,
    "cities_visited" : ["Paris", "Lille", "Dijon"], 
    "total_visits" : 12
  },
  {
    "country" :"Germany" ,
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits" : 5
  }
]

print(travel_log[0])

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score >= 90 and score <= 100:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"   

# 🚨 Don't change the code below 👇
print(student_grades)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    travel_log.append({"country" : country, "visits" : visits, "cities" : cities}) 



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
